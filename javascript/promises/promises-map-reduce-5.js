// https://developers.google.com/web/fundamentals/primers/promises#promisifying_xmlhttprequest

getJSON('story.json').then((story) => {
  addHtmlToPage(story.heading);

  // Map our array of chapter urls to
  // an array of chapter json promises.
  // This makes sure they are all downloaded in parallel.
  return story.chapterUrls.map(getJSON)
    .reduce((sequence, chapterPromise) => {
      return sequence
        .then(() => chapterPromise)
        .then((chapter) => {
          addHtmlToPage(chapter.html);
        });
    }, Promise.resolve());
}).then(() => {
  addTextToPage('All done');
}).catch((err) => {
  addTextToPage('Broken: ' + err.message);
}).then(() => {
  document.querySelector('.spinner').style.display = 'none';
});

