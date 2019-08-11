async function wait(ms) {
  await new Promise(resolve => setTimeout(() => resolve(), ms));
}

async function test() {
  await wait(1000);
  console.log('Hello, World!');
}

test();
