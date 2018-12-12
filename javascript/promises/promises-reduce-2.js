// https://developers.google.com/web/fundamentals/primers/promises#promisifying_xmlhttprequest

// Loop through our chapter urls
story.chapterUrls.reduce((sequence, chapterUrl) => {
  // Add these actions to the end of the sequence
  return sequence.then(() => {
    return getJSON(chapterUrl);
  }).then((chapter) => {
    addHtmlToPage(chapter.html);
  });
}, Promise.resolve());

