import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient()
const asyncGet = promisify(client.get).bind(client);
const asyncSet = promisify(client.set).bind(client);

client.on('connect', function () {
    console.log('Redis client connected to the server');
});
client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err.message}`);    
})

const setNewSchool = async (schoolName, value) => {
    try{
        const reply = await asyncSet(schoolName, value);
        console.log(`Reply: ${reply}`);
    } catch (err) {
        client.quit();
    }
}

const displaySchoolValue = async (schoolName) => {
    try {
        const reply = await asyncGet(schoolName);
        console.log(reply);
    } catch (err) {
        client.quit();
    }
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco')
