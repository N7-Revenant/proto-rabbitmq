use amqprs::{
    connection::{Connection, OpenConnectionArguments},
    callbacks::{DefaultConnectionCallback, DefaultChannelCallback},
    channel::BasicConsumeArguments
};
use tokio::{self, sync::Notify};
use tokio::io::Error as TError;
use std::str;

#[tokio::main]
async fn main() -> Result<(), Box<TError>> {
    let conn = Connection::open(&OpenConnectionArguments::new(
        "192.168.56.81",
        5672,
        "test",
        "test",
    ))
    .await.unwrap();
    conn.register_callback(DefaultConnectionCallback).await.unwrap();

    let ch = conn.open_channel(None).await.unwrap();
    ch.register_callback(DefaultChannelCallback).await.unwrap();

    let consumer_args = BasicConsumeArguments::new("hello", "some_id")
        .auto_ack(true)
        .finish();

    let consumer_result = ch.basic_consume_rx(consumer_args).await;
    if consumer_result.is_ok() {
        let (_ctag, mut rx) = consumer_result.unwrap();

        tokio::spawn(async move {
            while let Some(msg) = rx.recv().await {
                if let Some(payload) = msg.content {
                    println!(" [x] Received {:?}", str::from_utf8(&payload).unwrap());
                }
            };
    
        });

        println!(" [*] Waiting for messages. To exit press CTRL+C");
    
        let guard = Notify::new();
        guard.notified().await;
    }
    else {
        println!("ERROR!!!")
    }

    Ok(())
}