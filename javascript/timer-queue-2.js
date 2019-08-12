const TimerQueue = function() {

  let currentTimer = null;
  const tasks = [];

  function addTask(callback, delay) {
    tasks.push({ callback, delay, });
    if (!currentTimer) launchNextTask();
  }

  function launchNextTask() {
    if (currentTimer) return;
    const nextTask = tasks.shift();
    if (!nextTask) return clear();
    currentTimer = setTimeout(() => {
      nextTask.callback.call();
      currentTimer = null;
      launchNextTask();
    }, nextTask.delay);
  }

  function clear() {
    if (currentTimer) clearTimeout(currentTimer);
    currentTimer = null;
    tasks.length = 0;
  }

  return {
    addTask,
    clear,
  }
}

tq = TimerQueue();
tq.addTask(() => console.log('show snackbar'), 0);
tq.addTask(() => console.log('hide snackbar'), 1000);
tq.addTask(() => console.log('show snackbar 2'), 0);
tq.addTask(() => console.log('hide snackbar 2'), 1000);
