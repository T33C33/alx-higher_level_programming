#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completedTasks = {};
  body.forEach((task) => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId] += 1;
      }
    }
  });

  for (const userId in completedTasks) {
    console.log(`${userId}: ${completedTasks[userId]}`);
  }
});
