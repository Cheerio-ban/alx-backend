import redis from 'redis';

const client = redis.createClient();

client.on('connect', function () {
    console.log('Redis client connected to the server');
});
client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err.message}`);    
})

client.subscribe('holberton school channel');

client.on('message', (err, data) => {
    if (data === 'KILL_SERVER') {
        client.unsubscribe('holberton schoool channel');
        client.quit();
    }
    console.log(data);
})