import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
 };

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

// Event listeners for job completion and failure
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
