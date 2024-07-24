import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array (Number)', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });

  it('should throw an error if jobs is not an array (Object)', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });

  it('should throw an error if jobs is not an array (String)', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
  });

  it('should not throw an error if jobs is an empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.be.undefined;
  });

  it('should create two new jobs in the queue with correct details', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    });

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account',
    });
  });

  it('should not create jobs if the jobs array contains invalid job objects', () => {
    const invalidJobs = [
      { phoneNumber: 1234567890, message: 'Invalid message' }, // phoneNumber should be a string
      { phoneNumber: '4153118782' }, // Missing message
    ];
    
    createPushNotificationsJobs(invalidJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(0); // Expect no jobs to be created
  });

  it('should handle null or undefined jobs gracefully', () => {
    expect(() => {
      createPushNotificationsJobs(null, queue);
    }).to.throw('Jobs is not an array');

    expect(() => {
      createPushNotificationsJobs(undefined, queue);
    }).to.throw('Jobs is not an array');
  });

  it('should handle cases where the jobs array has missing properties', () => {
    const incompleteJobs = [
      { phoneNumber: '4153518780' }, // Missing message
    ];

    createPushNotificationsJobs(incompleteJobs, queue);
    expect(queue.testMode.jobs.length).to.equal(0); // Expect no jobs to be created
  });
});
