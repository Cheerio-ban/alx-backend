const createPushNotificationsJobs = (jobs, queue) => {
    if (!(jobs instanceof Array)) {
        throw new Error('Jobs is not an array');
    }
    for (let elem of jobs) {
        const job = queue.create('push_notification_code_3', elem).save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            }
        })

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`)
        })
        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`)
        })
        job.on('progress', () => {
            console.log(`Notification job ${job.id} ${percent}% complete`)
        })
    }
}

module.exports = createPushNotificationsJobs;
