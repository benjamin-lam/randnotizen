const initNavigation = () => {
  const toggle = document.querySelector('[data-nav-toggle]');
  const list = document.querySelector('[data-nav-list]');
  if (!toggle || !list) return;

  const closeMenu = () => {
    list.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    list.setAttribute('aria-expanded', String(!expanded));
  });

  list.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeMenu();
      toggle.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 960) {
      closeMenu();
    }
  });
};

const initAccordions = (root = document) => {
  root.querySelectorAll('[data-accordion] details').forEach((details) => {
    details.addEventListener('toggle', () => {
      if (details.open) {
        root
          .querySelectorAll('[data-accordion] details')
          .forEach((item) => {
            if (item !== details) item.removeAttribute('open');
          });
      }
    });
  });
};

const initTabs = (root = document) => {
  root.querySelectorAll('[role="tablist"]').forEach((tabList) => {
    const tabs = Array.from(tabList.querySelectorAll('[role="tab"]'));
    const panels = tabs.map((tab) => document.getElementById(tab.getAttribute('aria-controls')));

    const activateTab = (tab) => {
      tabs.forEach((item) => {
        const isSelected = item === tab;
        item.setAttribute('aria-selected', String(isSelected));
        item.tabIndex = isSelected ? 0 : -1;
      });

      panels.forEach((panel) => {
        panel.hidden = panel.id !== tab.getAttribute('aria-controls');
      });

      tab.focus();
    };

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => activateTab(tab));
      tab.addEventListener('keydown', (event) => {
        const index = tabs.indexOf(tab);
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
          event.preventDefault();
          activateTab(tabs[(index + 1) % tabs.length]);
        }
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
          event.preventDefault();
          activateTab(tabs[(index - 1 + tabs.length) % tabs.length]);
        }
      });
    });

    const selected = tabs.find((tab) => tab.getAttribute('aria-selected') === 'true') || tabs[0];
    activateTab(selected);
  });
};

const initOverlayToggle = () => {
  const triggers = document.querySelectorAll('[data-overlay-target]');
  triggers.forEach((trigger) => {
    const targetId = trigger.getAttribute('data-overlay-target');
    const overlay = document.getElementById(targetId);
    if (!overlay) return;

    const closeOverlay = () => {
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.removeProperty('overflow');
      trigger.focus();
    };

    trigger.addEventListener('click', () => {
      const hidden = overlay.getAttribute('aria-hidden') === 'true';
      overlay.setAttribute('aria-hidden', String(!hidden));
      document.body.style.setProperty('overflow', hidden ? 'hidden' : '');
      if (!hidden) {
        trigger.focus();
      } else {
        overlay.querySelector('[data-overlay-close]')?.focus();
      }
    });

    overlay.addEventListener('click', (event) => {
      if (event.target === overlay) {
        closeOverlay();
      }
    });

    overlay.querySelectorAll('[data-overlay-close]').forEach((closeButton) => {
      closeButton.addEventListener('click', closeOverlay);
    });

    overlay.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        closeOverlay();
      }
    });
  });
};

const initDropdownButtons = () => {
  document.querySelectorAll('[data-dropdown-button]').forEach((button) => {
    const menu = document.getElementById(button.getAttribute('aria-controls'));
    if (!menu) return;

    const close = () => {
      button.setAttribute('aria-expanded', 'false');
      menu.hidden = true;
    };

    button.addEventListener('click', () => {
      const expanded = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!expanded));
      menu.hidden = expanded;
      if (!expanded) {
        const firstLink = menu.querySelector('a, button, [tabindex="0"]');
        firstLink?.focus();
      }
    });

    button.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowDown') {
        event.preventDefault();
        const firstLink = menu.querySelector('a, button, [tabindex="0"]');
        firstLink?.focus();
      }
    });

    document.addEventListener('click', (event) => {
      if (!button.contains(event.target) && !menu.contains(event.target)) {
        close();
      }
    });

    menu.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        close();
        button.focus();
      }
    });

    close();
  });
};

const initScrollSpy = () => {
  const spyNav = document.querySelector('[data-scrollspy]');
  if (!spyNav) return;
  const links = spyNav.querySelectorAll('a[href^="#"]');
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const id = entry.target.getAttribute('id');
        const link = spyNav.querySelector(`a[href="#${id}"]`);
        if (link) {
          link.setAttribute('aria-current', entry.isIntersecting ? 'true' : 'false');
        }
      });
    },
    { rootMargin: '-40% 0px -55% 0px', threshold: [0, 1] }
  );

  links.forEach((link) => {
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      observer.observe(target);
    }
  });
};

const initProgressiveEnhancements = () => {
  initNavigation();
  initAccordions();
  initTabs();
  initOverlayToggle();
  initDropdownButtons();
  initScrollSpy();
};

if (document.readyState !== 'loading') {
  initProgressiveEnhancements();
} else {
  document.addEventListener('DOMContentLoaded', initProgressiveEnhancements);
}
