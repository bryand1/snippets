const myAsyncFunction = async () => {
  await new Promise((resolve, reject) => setTimeout(() => resolve(), 2000));
  console.log('Hello, World!');
}

/* This will finish before the function above */
const myAsyncFunction2 = async () => {
  try {
    await new Promise((resolve, reject) => setTimeout(() => reject(new Error('Hold up!')), 200));
  } catch(e) {
    console.error(e.message);
  }
}

myAsyncFunction();
myAsyncFunction2();

