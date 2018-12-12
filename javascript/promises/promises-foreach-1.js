// https://developers.google.com/web/fundamentals/primers/promises#promisifying_xmlhttprequest

var sequence = Promise.resolve();

// Loop through our chapter urls
story.chapterUrls.forEach((chapterUrl) => {
  // Add these actions to the end of the sequence
  sequence = sequence.then(() => getJSON(chapterUrl)).then((chapter) => {
    addHtmlToPage(chapter.html);
  });
});

