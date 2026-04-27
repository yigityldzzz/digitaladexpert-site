export async function onRequest({ request, next }) {
  const url = new URL(request.url);

  if (url.hostname === 'promptkit.digitaladexpert.de') {
    // Already on a promptkit path — serve directly
    if (url.pathname.startsWith('/promptkit/')) {
      return next();
    }
    // Rewrite root and other paths to /promptkit/
    const newPath = '/promptkit' + (url.pathname === '/' ? '/' : url.pathname);
    url.pathname = newPath;
    return Response.redirect(url.toString(), 301);
  }

  return next();
}
