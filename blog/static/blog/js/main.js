document.addEventListener('DOMContentLoaded', function () {
  var navToggle = document.querySelector('[data-nav-toggle]');
  var nav = document.getElementById('site-nav');

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  var drawer = document.getElementById('categories-drawer');
  var overlay = document.querySelector('[data-drawer-overlay]');
  var openers = document.querySelectorAll('[data-drawer-open]');
  var closers = document.querySelectorAll('[data-drawer-close]');

  function openDrawer() {
    if (!drawer || !overlay) return;
    drawer.classList.add('is-open');
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (!drawer || !overlay) return;
    drawer.classList.remove('is-open');
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  openers.forEach(function (btn) {
    btn.addEventListener('click', openDrawer);
  });

  closers.forEach(function (btn) {
    btn.addEventListener('click', closeDrawer);
  });

  if (overlay) {
    overlay.addEventListener('click', closeDrawer);
  }

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      closeDrawer();
      if (nav) {
        nav.classList.remove('is-open');
        if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
      }
    }
  });

  var loadMoreBtn = document.getElementById('load-more-btn');
  var articleList = document.getElementById('article-list');

  if (loadMoreBtn && articleList) {
    loadMoreBtn.addEventListener('click', function () {
      var url = new URL(loadMoreBtn.dataset.url, window.location.origin);
      url.searchParams.set('page', loadMoreBtn.dataset.nextPage);
      if (loadMoreBtn.dataset.categoria) {
        url.searchParams.set('categoria', loadMoreBtn.dataset.categoria);
      }

      loadMoreBtn.disabled = true;

      fetch(url, { headers: { 'X-Requested-With': 'fetch' } })
        .then(function (response) {
          var hasNext = response.headers.get('X-Has-Next') === 'true';
          var nextPage = response.headers.get('X-Next-Page');
          return response.text().then(function (html) {
            articleList.insertAdjacentHTML('beforeend', html);
            if (hasNext && nextPage) {
              loadMoreBtn.dataset.nextPage = nextPage;
              loadMoreBtn.disabled = false;
            } else {
              loadMoreBtn.closest('.load-more').remove();
            }
          });
        })
        .catch(function () {
          loadMoreBtn.disabled = false;
        });
    });
  }
});
