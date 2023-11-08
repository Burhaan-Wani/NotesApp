var staticCacheName = "djangopwa-v1";

self.oninstall = function (evt) {
    evt.waitUntil(
        caches.open(staticCacheName).then(function (cache) {
            return Promise.all(
                ["/", "Login.html"].map(function (url) {
                    return fetch(new Request(url, { redirect: "manual" })).then(
                        function (res) {
                            return cache.put(url, res);
                        }
                    );
                })
            );
        })
    );
};
self.fetch = function (evt) {
    var url = new URL(evt.request.url);
    if (url.pathname != "/" && url.pathname != "Login.html") return;
    evt.respondWith(caches.match(evt.request, { cacheName: staticCacheName }));
};
