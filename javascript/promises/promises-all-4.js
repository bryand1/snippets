// https://developers.google.com/web/fundamentals/primers/promises#promisifying_xmlhttprequest
Promise.all(arrayOfPromises).then((arrayOfResults) => {
  //...
});

/*
 * Promise.all takes an array of promises and creates a promise that fulfills when all of them
 * successfully complete. You get an array of results (whatever the promises fulfilled to) in
 * the same order as the promises you passed in.
 */

getJSON('story.json').then((story) => {
  addHtmlToPage(story.heading);

  return Promise.all(story.chapterUrls.map(getJSON));
}).then((chapters) => {
  chapters.forEach((chapter) => { addHtmlToPage(chapter.html); });
  addTextToPage('All done');
}).catch((err) => { 
  addTextToPage('Broken: ' + err.message);
}).then(() => {
  document.querySelector('.spinner').style.display = 'none';
});

