import { createClient, print } from 'redis';

// Setting up the client
async function setupClient() {
  const client = createClient();

  // Error handling
  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`, err));

  await client.connect();
  console.log('Redis client connected to the server');

  // Define functions to interact with Redis after the client is connected
  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);  // Using redis.print for confirmation message
  }

  function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, res) => {
      if (err) {
        console.log(err);
      } else {
        console.log(res);
      }
    });
  }

  // Call the functions after client setup
  // console.log('Calling displaySchoolValue for "Holberton"');
  displaySchoolValue('Holberton');

  // console.log('Calling setNewSchool for "HolbertonSanFrancisco"');
  setNewSchool('HolbertonSanFrancisco', '100');

  // console.log('Calling displaySchoolValue for "HolbertonSanFrancisco"');
  displaySchoolValue('HolbertonSanFrancisco');
}

// Execute the setupClient function
setupClient();
