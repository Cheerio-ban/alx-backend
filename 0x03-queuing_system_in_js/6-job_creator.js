import kue from 'kue';

const queue = kue.createQueue()

const obj = {
    phoneNumber: '8067857645',
    message: 'Take tech seriously and write code yourself',
};

const job = queue.create('push_notification_code', obj).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`)
    } else {
        console.log('Notification job failed');
    }
})

job.on('complete', () => {
    console.log('Notification job completed');
});
