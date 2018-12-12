getJSON('story.json').then((story) => {
  addHtmlToPage(story.heading);

  return story.chapterUrls.reduce((sequence, chapterUrl) => {
    // Once the last chapter's promise is done...
    return sequence
      .then(() => getJSON(chapterUrl))
      .then((chapter) => { addHtmlToPage(chapter.html); });
  }, Promise.resolve());
})
  .then(() => addTextToPage('All done'))
  .catch(err => addTextToPage('Broken: ' + err.message))
  .then(() => { document.querySelector('.spinner').style.display = 'none'; });

