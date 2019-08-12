// https://codereview.stackexchange.com/questions/148363/time-delayed-function-queue
function TimerQueue(){
  this.currentTimer = null;
  this.tasks = [];
}

TimerQueue.prototype.addTask = function(callback, delay) {
  this.tasks.push({ callback: callback, delay: delay });

  // If there's a scheduled task, bail out.
  if(this.currentTimer) return;

  // Otherwise, start kicking tires
  this.launchNextTask();
};

TimerQueue.prototype.launchNextTask = function(){
  // If there's a scheduled task, bail out.
  if(this.currentTimer) return;

  var nextTask = this.tasks.shift();

  // There's no more tasks, clean up.
  if(!nextTask) return this.clear();

  // Otherwise, schedule the next task.
  var self = this;
  this.currentTimer = setTimeout(function(){
    nextTask.callback.call();

    self.currentTimer = null;

    // Call this function again to set up the next task.
    self.launchNextTask();
  }, nextTask.delay);
};

TimerQueue.prototype.clear = function(){
  if (this.currentTimer) clearTimeout(this.currentTimer);

  // Timer clears only destroy the timer. It doesn't null references.
  this.currentTimer = null;

  // Fast way to clear the task queue
  this.tasks.length = 0;
};

tq = new TimerQueue();
tq.addTask(() => console.log(1000), 1000);
tq.addTask(() => console.log(3000), 2000);
tq.addTask(() => console.log(7000), 4000);
