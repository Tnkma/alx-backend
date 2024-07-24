import { createClient } from 'redis';
import { promisify } from 'util';

// Setting up the client
async function setupClient() {
  const client = createClient();

  // Error handling
  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`, err));

  await client.connect();
  console.log('Redis client connected to the server');

  // Promisify the get method
  const getAsync = promisify(client.get).bind(client);

  // Define functions to interact with Redis after the client is connected
  async function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, res) => {
      if (err) {
        console.log(err);
      } else {
        console.log(`Set operation result for ${schoolName}: ${res}`);
      }
    });
  }

  async function displaySchoolValue(schoolName) {
    try {
      const res = await getAsync(schoolName);
      console.log(`Get operation result for ${schoolName}: ${res}`);
    } catch (err) {
      console.log(err);
    }
  }

  // Call the functions after client setup
  // console.log('Calling displaySchoolValue for "Holberton"');
  await displaySchoolValue('Holberton');

  // console.log('Calling setNewSchool for "HolbertonSanFrancisco"');
  await setNewSchool('HolbertonSanFrancisco', '100');

  // console.log('Calling displaySchoolValue for "HolbertonSanFrancisco"');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Execute the setupClient function
setupClient();
