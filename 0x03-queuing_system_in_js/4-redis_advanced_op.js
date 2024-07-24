import { createClient, print } from 'redis';

//setting up the client
async function setupClient() {
  const client = createClient();

  // Error handling
  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`, err));

  await client.connect();
  console.log('Redis client connected to the server');

  const KEY = 'HolbertonSchools';

  const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
  const values = [50, 80, 20, 20, 40, 2];
  
  keys.forEach((key, index) => {
    client.hset(KEY, key, values[index], print);
  });
  
  client.hgetall(KEY, (err, value) => {
    console.log(value);
  });
}


setupClient();
