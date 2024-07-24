import { createClient } from 'redis';

//setting up the client
async function setupClient() {
  const client = createClient();

  // Error handling
  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`, err));

  await client.connect();
  console.log('Redis client connected to the server');

  const CHANNEL = 'holberton school channel';

  client.subscribe(CHANNEL);

  client.on('message', (channel, message) => {
    if (channel === CHANNEL) console.log(message);

    if (message === 'KILL_SERVER') {
      client.unsubscribe(CHANNEL);
      client.quit();
    }
  });
}


setupClient();
