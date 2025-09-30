const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

const focusableSelectors = [
  'a[href]',
  'button:not([disabled])',
  'input:not([disabled])',
  'select:not([disabled])',
  'textarea:not([disabled])',
  '[tabindex]:not([tabindex="-1"])'
];

function initCopyButtons() {
  document.querySelectorAll('[data-copy-button]').forEach((button) => {
    button.addEventListener('click', async () => {
      const targetId = button.getAttribute('data-copy-target');
      const target = document.getElementById(targetId);
      if (!target) return;
      const text = target.textContent || '';
      try {
        await navigator.clipboard.writeText(text.trim());
        const feedback = button.closest('[data-code-snippet], figure')?.querySelector('[data-copy-feedback]');
        if (feedback) {
          feedback.textContent = 'Code in Zwischenablage kopiert.';
        }
        button.classList.add('is-active');
        button.setAttribute('aria-live', 'polite');
        button.textContent = 'Kopiert!';
        setTimeout(() => {
          button.textContent = 'Code kopieren';
          button.classList.remove('is-active');
        }, 1800);
      } catch (error) {
        console.error('Clipboard fehlgeschlagen', error);
      }
    });
  });
}

function initAudioPlayers() {
  document.querySelectorAll('[data-audio-player]').forEach((player) => {
    const audio = player.querySelector('[data-audio-element]');
    const tracks = Array.from(player.querySelectorAll('[data-audio-track]'));
    const status = player.querySelector('#audio-status');

    tracks.forEach((track) => {
      track.addEventListener('click', () => {
        const src = track.getAttribute('data-src');
        if (!src || !audio) return;
        const wasPlaying = !audio.paused;
        audio.src = src;
        audio.currentTime = 0;
        if (wasPlaying) {
          audio.play().catch(() => undefined);
        }
        tracks.forEach((btn) => {
          btn.classList.toggle('is-current', btn === track);
          btn.setAttribute('aria-pressed', btn === track ? 'true' : 'false');
        });
        if (status) {
          const title = track.getAttribute('data-title') || 'Episode';
          status.textContent = `${title} wird abgespielt.`;
        }
      });
    });
  });
}

function initContactForm() {
  document.querySelectorAll('[data-contact-form]').forEach((form) => {
    const feedback = form.querySelector('[data-form-feedback]');
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const formData = new FormData(form);
      const name = (formData.get('name') || '').toString().trim();
      const email = (formData.get('email') || '').toString().trim();
      if (name.length < 2) {
        if (feedback) feedback.textContent = 'Bitte geben Sie einen gültigen Namen ein.';
        return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        if (feedback) feedback.textContent = 'Bitte geben Sie eine gültige E-Mail-Adresse ein.';
        return;
      }
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      if (feedback) {
        feedback.textContent = 'Vielen Dank! Wir melden uns innerhalb von 24 Stunden.';
      }
      form.reset();
    });
  });
}

function initCookieBanner() {
  const banner = document.querySelector('[data-cookie-banner]');
  if (!banner) return;
  const STORAGE_KEY = 'content-elements-consent';
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      banner.hidden = true;
      return;
    }
  } catch (error) {
    console.warn('Consent konnte nicht gelesen werden', error);
  }

  banner.querySelectorAll('[data-consent-action]').forEach((button) => {
    button.addEventListener('click', () => {
      const action = button.getAttribute('data-consent-action');
      try {
        localStorage.setItem(STORAGE_KEY, action || 'unknown');
      } catch (error) {
        console.warn('Consent konnte nicht gespeichert werden', error);
      }
      banner.hidden = true;
    });
  });

  banner.querySelector('[data-consent-open-settings]')?.addEventListener('click', () => {
    const details = banner.querySelector('details');
    if (details) {
      details.open = true;
      details.focus();
    }
  });
}

function formatDate(date) {
  return date.toLocaleDateString('de-DE');
}

function buildCalendarDays(baseDate) {
  const firstDay = new Date(baseDate.getFullYear(), baseDate.getMonth(), 1);
  const startDay = (firstDay.getDay() + 6) % 7; // Montag als erster Tag
  const daysInMonth = new Date(baseDate.getFullYear(), baseDate.getMonth() + 1, 0).getDate();
  const previousMonthDays = new Date(baseDate.getFullYear(), baseDate.getMonth(), 0).getDate();
  const cells = [];
  for (let i = 0; i < 42; i += 1) {
    const dayNumber = i - startDay + 1;
    let date;
    let muted = false;
    if (dayNumber < 1) {
      date = new Date(baseDate.getFullYear(), baseDate.getMonth() - 1, previousMonthDays + dayNumber);
      muted = true;
    } else if (dayNumber > daysInMonth) {
      date = new Date(baseDate.getFullYear(), baseDate.getMonth() + 1, dayNumber - daysInMonth);
      muted = true;
    } else {
      date = new Date(baseDate.getFullYear(), baseDate.getMonth(), dayNumber);
    }
    cells.push({ date, muted });
  }
  return cells;
}

function initDatePickers() {
  document.querySelectorAll('[data-date-picker]').forEach((picker) => {
    const input = picker.querySelector('[data-date-input]');
    const grid = picker.querySelector('[data-calendar-grid]');
    const title = picker.querySelector('[data-calendar-title]');
    if (!grid || !input || !title) return;

    const startMonth = picker.getAttribute('data-start-month');
    let activeDate = startMonth ? new Date(`${startMonth}-01T00:00:00`) : new Date();
    let selectedDate = new Date();

    function render(date) {
      title.textContent = date.toLocaleDateString('de-DE', { month: 'long', year: 'numeric' });
      grid.innerHTML = '';
      const cells = buildCalendarDays(date);
      cells.forEach((cell, index) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.textContent = String(cell.date.getDate());
        button.dataset.timestamp = cell.date.toISOString();
        button.dataset.index = String(index);
        button.classList.toggle('is-muted', cell.muted);
        const isToday = cell.date.toDateString() === new Date().toDateString();
        button.classList.toggle('is-today', isToday);
        const isSelected = selectedDate && cell.date.toDateString() === selectedDate.toDateString();
        button.classList.toggle('is-selected', isSelected);
        button.setAttribute('role', 'gridcell');
        button.setAttribute('aria-selected', isSelected ? 'true' : 'false');
        if (index === 0 || isSelected) {
          button.tabIndex = 0;
        } else {
          button.tabIndex = -1;
        }
        button.addEventListener('click', () => {
          selectedDate = new Date(button.dataset.timestamp || '');
          input.value = formatDate(selectedDate);
          render(activeDate);
        });
        button.addEventListener('keydown', (event) => {
          const currentIndex = Number(button.dataset.index);
          let nextIndex = currentIndex;
          if (event.key === 'ArrowRight') nextIndex += 1;
          if (event.key === 'ArrowLeft') nextIndex -= 1;
          if (event.key === 'ArrowDown') nextIndex += 7;
          if (event.key === 'ArrowUp') nextIndex -= 7;
          if (event.key === 'Home') nextIndex -= currentIndex % 7;
          if (event.key === 'End') nextIndex += 6 - (currentIndex % 7);
          if (event.key === 'PageDown') {
            activeDate = new Date(activeDate.getFullYear(), activeDate.getMonth() + 1, 1);
            render(activeDate);
            setTimeout(() => {
              grid.querySelector('button[data-index="0"]')?.focus();
            }, 0);
            event.preventDefault();
            return;
          }
          if (event.key === 'PageUp') {
            activeDate = new Date(activeDate.getFullYear(), activeDate.getMonth() - 1, 1);
            render(activeDate);
            setTimeout(() => {
              grid.querySelector('button[data-index="0"]')?.focus();
            }, 0);
            event.preventDefault();
            return;
          }
          const buttons = grid.querySelectorAll('button');
          if (nextIndex >= 0 && nextIndex < buttons.length) {
            const nextButton = buttons[nextIndex];
            nextButton.focus();
            event.preventDefault();
          }
        });
        grid.appendChild(button);
      });
    }

    render(activeDate);

    picker.querySelector('[data-calendar-prev]')?.addEventListener('click', () => {
      activeDate = new Date(activeDate.getFullYear(), activeDate.getMonth() - 1, 1);
      render(activeDate);
    });

    picker.querySelector('[data-calendar-next]')?.addEventListener('click', () => {
      activeDate = new Date(activeDate.getFullYear(), activeDate.getMonth() + 1, 1);
      render(activeDate);
    });
  });
}

function initDropdowns() {
  document.querySelectorAll('[data-dropdown]').forEach((dropdown) => {
    const toggle = dropdown.querySelector('[data-dropdown-toggle]');
    const list = dropdown.querySelector('[data-dropdown-list]');
    const hiddenInput = dropdown.querySelector('[data-dropdown-input]');
    const label = dropdown.querySelector('[data-dropdown-label]');
    if (!toggle || !list || !hiddenInput || !label) return;

    let isOpen = false;
    const options = Array.from(list.querySelectorAll('.dropdown__option'));

    function close() {
      isOpen = false;
      dropdown.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      list.setAttribute('hidden', 'true');
    }

    function open() {
      isOpen = true;
      dropdown.classList.add('is-open');
      toggle.setAttribute('aria-expanded', 'true');
      list.removeAttribute('hidden');
      options.find((option) => option.getAttribute('aria-selected') === 'true')?.focus();
    }

    toggle.addEventListener('click', () => {
      if (isOpen) {
        close();
      } else {
        open();
      }
    });

    toggle.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
        event.preventDefault();
        open();
      }
    });

    options.forEach((option) => {
      option.addEventListener('click', () => {
        options.forEach((opt) => opt.setAttribute('aria-selected', 'false'));
        option.setAttribute('aria-selected', 'true');
        hiddenInput.value = option.dataset.value || option.textContent || '';
        label.textContent = option.textContent || '';
        close();
        toggle.focus();
      });

      option.addEventListener('keydown', (event) => {
        const currentIndex = options.indexOf(option);
        if (event.key === 'ArrowDown') {
          options[(currentIndex + 1) % options.length].focus();
          event.preventDefault();
        }
        if (event.key === 'ArrowUp') {
          options[(currentIndex - 1 + options.length) % options.length].focus();
          event.preventDefault();
        }
        if (event.key === 'Escape') {
          close();
          toggle.focus();
        }
      });
    });

    document.addEventListener('click', (event) => {
      if (!dropdown.contains(event.target)) {
        close();
      }
    });
  });
}

function initFileUploader() {
  document.querySelectorAll('[data-file-uploader]').forEach((section) => {
    const dropzone = section.querySelector('[data-dropzone]');
    const input = section.querySelector('[data-file-input]');
    const list = section.querySelector('[data-upload-list]');
    if (!dropzone || !input || !list) return;

    function handleFiles(files) {
      Array.from(files).forEach((file) => {
        const item = document.createElement('div');
        item.className = 'upload-item';
        item.innerHTML = `
          <span>${file.name}</span>
          <div class="stack-sm" style="min-width:120px;">
            <div class="progress-bar"><div class="progress-bar__fill"></div></div>
            <span class="text-muted" data-upload-status>Lädt hoch …</span>
          </div>
        `;
        list.append(item);
        const bar = item.querySelector('.progress-bar__fill');
        const status = item.querySelector('[data-upload-status]');
        let progress = 0;
        const timer = setInterval(() => {
          progress += 10;
          bar.style.width = `${progress}%`;
          if (progress >= 100) {
            clearInterval(timer);
            if (status) status.textContent = 'Fertig';
          }
        }, prefersReducedMotion.matches ? 120 : 80);
      });
    }

    dropzone.addEventListener('dragover', (event) => {
      event.preventDefault();
      dropzone.classList.add('is-dragover');
    });
    dropzone.addEventListener('dragleave', () => dropzone.classList.remove('is-dragover'));
    dropzone.addEventListener('drop', (event) => {
      event.preventDefault();
      dropzone.classList.remove('is-dragover');
      if (event.dataTransfer?.files) {
        handleFiles(event.dataTransfer.files);
      }
    });
    dropzone.addEventListener('click', () => input.click());
    input.addEventListener('change', () => {
      if (input.files) {
        handleFiles(input.files);
      }
    });
  });
}

function initCarousel() {
  document.querySelectorAll('[data-carousel]').forEach((carousel) => {
    const track = carousel.querySelector('[data-carousel-track]');
    const slides = track ? Array.from(track.querySelectorAll('[data-carousel-slide]')) : [];
    const dotsContainer = carousel.nextElementSibling?.matches('[data-carousel-dots]') ? carousel.nextElementSibling : carousel.querySelector('[data-carousel-dots]');
    const dots = dotsContainer ? Array.from(dotsContainer.querySelectorAll('[role="tab"]')) : [];
    if (!track || slides.length === 0) return;
    let index = 0;

    function update(newIndex) {
      index = (newIndex + slides.length) % slides.length;
      track.style.transform = `translateX(-${index * 100}%)`;
      slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === index;
        slide.setAttribute('aria-hidden', isActive ? 'false' : 'true');
      });
      dots.forEach((dot, dotIndex) => {
        dot.setAttribute('aria-current', dotIndex === index ? 'true' : 'false');
      });
    }

    carousel.querySelector('[data-carousel-prev]')?.addEventListener('click', () => update(index - 1));
    carousel.querySelector('[data-carousel-next]')?.addEventListener('click', () => update(index + 1));
    dots.forEach((dot, dotIndex) => {
      dot.addEventListener('click', () => update(dotIndex));
    });

    let autoSlide;
    function startAuto() {
      if (prefersReducedMotion.matches) return;
      autoSlide = window.setInterval(() => update(index + 1), 6000);
    }
    function stopAuto() {
      if (autoSlide) window.clearInterval(autoSlide);
    }
    carousel.addEventListener('mouseenter', stopAuto);
    carousel.addEventListener('mouseleave', startAuto);
    startAuto();
    update(0);
  });
}

function initInputHelpers() {
  document.querySelectorAll('[data-input-with-counter]').forEach((input) => {
    const wrapper = input.closest('.input-group');
    const output = wrapper?.querySelector('[data-input-counter]');
    if (!output) return;
    const max = Number(input.getAttribute('maxlength')) || 20;
    input.addEventListener('input', () => {
      output.textContent = String(input.value.length);
      if (input.value.length > max) {
        input.classList.add('input--invalid');
      } else {
        input.classList.remove('input--invalid');
      }
    });
  });

  document.querySelectorAll('[data-toggle-password]').forEach((button) => {
    button.addEventListener('click', () => {
      const input = button.previousElementSibling;
      if (!(input instanceof HTMLInputElement)) return;
      if (input.type === 'password') {
        input.type = 'text';
        button.textContent = 'Verbergen';
      } else {
        input.type = 'password';
        button.textContent = 'Anzeigen';
      }
      input.focus();
    });
  });
}

function initMiniCart() {
  document.querySelectorAll('[data-mini-cart]').forEach((cart) => {
    const totalEl = cart.querySelector('[data-cart-total]');
    const items = cart.querySelectorAll('[data-cart-item]');

    function formatCurrency(value) {
      return new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(value);
    }

    function updateTotal() {
      let total = 0;
      items.forEach((item) => {
        const price = Number(item.querySelector('[data-item-price]')?.getAttribute('data-item-price'));
        const quantity = Number(item.querySelector('[data-item-qty]')?.value || 1);
        if (!Number.isNaN(price)) {
          total += price * quantity;
        }
      });
      if (totalEl) totalEl.textContent = formatCurrency(total);
    }

    items.forEach((item) => {
      const qty = item.querySelector('[data-item-qty]');
      qty?.addEventListener('input', updateTotal);
    });

    updateTotal();
  });
}

function getFocusableElements(container) {
  return Array.from(container.querySelectorAll(focusableSelectors.join(',')));
}

function trapFocus(dialog) {
  const focusables = getFocusableElements(dialog);
  if (focusables.length === 0) return;
  const first = focusables[0];
  const last = focusables[focusables.length - 1];
  dialog.addEventListener('keydown', (event) => {
    if (event.key !== 'Tab') return;
    if (event.shiftKey && document.activeElement === first) {
      last.focus();
      event.preventDefault();
    } else if (!event.shiftKey && document.activeElement === last) {
      first.focus();
      event.preventDefault();
    }
  });
}

function initModals() {
  document.querySelectorAll('[data-open-modal]').forEach((trigger) => {
    const targetSelector = trigger.getAttribute('data-open-modal');
    const dialog = targetSelector ? document.querySelector(targetSelector) : null;
    if (!(dialog instanceof HTMLDialogElement)) return;
    const closeButtons = dialog.querySelectorAll('[data-close-modal]');
    trapFocus(dialog);

    function open() {
      if (typeof dialog.showModal === 'function') {
        dialog.showModal();
      } else {
        dialog.setAttribute('open', 'true');
      }
      dialog.addEventListener('cancel', (event) => event.preventDefault());
      const firstFocusable = getFocusableElements(dialog)[0];
      firstFocusable?.focus();
    }

    function close() {
      if (typeof dialog.close === 'function') {
        dialog.close();
      } else {
        dialog.removeAttribute('open');
      }
      trigger.focus();
    }

    trigger.addEventListener('click', () => open());
    closeButtons.forEach((btn) => btn.addEventListener('click', () => close()));
    dialog.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        close();
      }
    });
  });
}

function initWizard() {
  document.querySelectorAll('[data-wizard]').forEach((wizard) => {
    const steps = Array.from(wizard.querySelectorAll('[data-wizard-step]'));
    const indicators = wizard.querySelectorAll('.wizard__step');
    let index = 0;

    function update() {
      steps.forEach((step, stepIndex) => {
        step.hidden = stepIndex !== index;
      });
      indicators.forEach((indicator, indicatorIndex) => {
        indicator.setAttribute('aria-current', indicatorIndex === index ? 'step' : 'false');
      });
    }

    wizard.querySelectorAll('[data-wizard-next]').forEach((button) => {
      button.addEventListener('click', () => {
        index = Math.min(index + 1, steps.length - 1);
        update();
      });
    });

    wizard.querySelectorAll('[data-wizard-prev]').forEach((button) => {
      button.addEventListener('click', () => {
        index = Math.max(index - 1, 0);
        update();
      });
    });

    steps.forEach((step) => {
      step.addEventListener('submit', (event) => {
        event.preventDefault();
        index = Math.min(index + 1, steps.length - 1);
        update();
      });
    });

    update();
  });
}

function initNewsletterForms() {
  const forms = document.querySelectorAll('[data-newsletter], [data-newsletter-modal]');
  forms.forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const emailInput = form.querySelector('input[type="email"]');
      const feedback = form.closest('form')?.querySelector('[data-newsletter-feedback]') || form.querySelector('[data-newsletter-feedback]');
      if (emailInput && !emailInput.value.includes('@')) {
        if (feedback) feedback.textContent = 'Bitte geben Sie eine gültige E-Mail-Adresse ein.';
        emailInput.focus();
        return;
      }
      if (feedback) feedback.textContent = 'Checken Sie Ihr Postfach für die Bestätigung.';
      form.reset();
    });
  });
}

function initNotificationBanner() {
  document.querySelectorAll('[data-notification-banner]').forEach((banner) => {
    banner.querySelector('[data-dismiss-banner]')?.addEventListener('click', () => {
      banner.setAttribute('hidden', 'true');
    });
  });
}

function initPopovers() {
  document.querySelectorAll('[data-popover]').forEach((popover) => {
    const toggle = popover.querySelector('[data-popover-toggle]');
    const panel = popover.querySelector('.popover__panel');
    if (!toggle || !panel) return;
    let open = false;

    function close() {
      open = false;
      popover.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      panel.setAttribute('hidden', 'true');
    }

    function show() {
      open = true;
      popover.classList.add('is-open');
      toggle.setAttribute('aria-expanded', 'true');
      panel.removeAttribute('hidden');
      panel.focus?.();
    }

    toggle.addEventListener('click', () => {
      if (open) {
        close();
      } else {
        show();
      }
    });

    popover.querySelector('[data-popover-close]')?.addEventListener('click', () => close());

    document.addEventListener('click', (event) => {
      if (!popover.contains(event.target)) {
        close();
      }
    });
  });
}

function initReviewForms() {
  document.querySelectorAll('[data-review-form]').forEach((form) => {
    const output = form.querySelector('[data-rating-output]');
    const radios = Array.from(form.querySelectorAll('input[name="rating"]'));
    radios.forEach((radio) => {
      radio.addEventListener('change', () => {
        if (output) output.textContent = radio.value;
      });
    });
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const feedback = form.querySelector('[data-review-feedback]');
      if (feedback) feedback.textContent = 'Danke für Ihr Feedback!';
      form.reset();
      if (output) output.textContent = '0';
    });
  });
}

function initSearch() {
  const data = [
    'Accessibility',
    'Design Tokens',
    'Komponenten Bibliothek',
    'Content Strategie',
    'Onboarding Flow',
    'Team Collaboration'
  ];
  document.querySelectorAll('[data-search]').forEach((form) => {
    const input = form.querySelector('[data-search-input]');
    const list = form.querySelector('[data-search-suggestions]');
    if (!input || !list) return;

    input.addEventListener('input', () => {
      const query = input.value.trim().toLowerCase();
      list.innerHTML = '';
      if (query.length < 2) return;
      const matches = data.filter((item) => item.toLowerCase().includes(query)).slice(0, 5);
      matches.forEach((match) => {
        const li = document.createElement('li');
        li.textContent = match;
        li.role = 'option';
        list.append(li);
      });
    });
  });
}

function initShareButtons() {
  document.querySelectorAll('[data-share-buttons]').forEach((group) => {
    const feedback = group.querySelector('[data-share-feedback]');
    group.querySelectorAll('[data-share-action]').forEach((button) => {
      button.addEventListener('click', async () => {
        const action = button.getAttribute('data-share-action');
        if (action === 'native' && navigator.share) {
          try {
            await navigator.share({
              title: document.title,
              url: window.location.href
            });
          } catch (error) {
            console.warn('Native Share abgebrochen', error);
          }
        } else {
          await navigator.clipboard.writeText(window.location.href);
          if (feedback) feedback.textContent = 'Link kopiert';
        }
      });
    });
  });
}

function initTableOfContents() {
  document.querySelectorAll('[data-toc]').forEach((toc) => {
    const toggle = toc.querySelector('[data-toc-toggle]');
    const list = toc.querySelector('[data-toc-list]');
    if (!toggle || !list) return;
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      if (expanded) {
        list.hidden = true;
      } else {
        list.hidden = false;
      }
    });
  });
}

function initToast() {
  document.querySelectorAll('[data-toast-trigger]').forEach((button) => {
    const region = button.closest('.stack-md')?.querySelector('[data-toast-region]');
    if (!region) return;
    button.addEventListener('click', () => {
      const toast = document.createElement('div');
      toast.className = 'toast';
      toast.innerHTML = '<strong>Gespeichert!</strong><span>Ihre Einstellungen wurden aktualisiert.</span>';
      region.append(toast);
      setTimeout(() => {
        toast.classList.add('is-leaving');
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    });
  });
}

function initTooltip() {
  document.querySelectorAll('[data-tooltip]').forEach((tooltip) => {
    const trigger = tooltip.querySelector('[data-tooltip-trigger]');
    if (!trigger) return;
    const bubble = tooltip.querySelector('.tooltip__bubble');
    function show() {
      tooltip.setAttribute('aria-expanded', 'true');
      bubble?.setAttribute('aria-hidden', 'false');
    }
    function hide() {
      tooltip.setAttribute('aria-expanded', 'false');
      bubble?.setAttribute('aria-hidden', 'true');
    }
    trigger.addEventListener('focus', show);
    trigger.addEventListener('blur', hide);
    trigger.addEventListener('mouseenter', show);
    trigger.addEventListener('mouseleave', hide);
  });
}

function initReviewStars() {
  // No JS required currently but kept for future extension
}

function initSearchFormSubmission() {
  document.querySelectorAll('[data-search]').forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const input = form.querySelector('[data-search-input]');
      const feedback = form.querySelector('[data-search-feedback]');
      if (input && feedback) {
        feedback.textContent = `Suche gestartet für „${input.value.trim()}“`;
      }
    });
  });
}

function initShareFallbacks() {
  if (!navigator.share) {
    document.querySelectorAll('[data-share-action="native"]').forEach((button) => {
      button.textContent = 'Link teilen';
    });
  }
}

function initSearchSuggestionsRole() {
  document.querySelectorAll('[data-search-suggestions]').forEach((list) => {
    list.setAttribute('role', 'listbox');
  });
}

function initToastRegion() {
  document.querySelectorAll('[data-toast-region]').forEach((region) => {
    region.setAttribute('aria-live', 'polite');
  });
}

function initDropdownAccessibility() {
  document.querySelectorAll('[data-dropdown]').forEach((dropdown) => {
    const list = dropdown.querySelector('[data-dropdown-list]');
    if (list) list.hidden = true;
  });
}

function initSearchPrefill() {
  const params = new URLSearchParams(window.location.search);
  const query = params.get('q');
  if (query) {
    const input = document.querySelector('[data-search-input]');
    if (input) input.value = query;
  }
}

function initTooltipAria() {
  document.querySelectorAll('[data-tooltip]').forEach((tooltip) => {
    tooltip.querySelector('.tooltip__bubble')?.setAttribute('aria-hidden', 'true');
  });
}

function initDropdownEscape() {
  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    document.querySelectorAll('[data-dropdown]').forEach((dropdown) => {
      dropdown.classList.remove('is-open');
      dropdown.querySelector('[data-dropdown-toggle]')?.setAttribute('aria-expanded', 'false');
      dropdown.querySelector('[data-dropdown-list]')?.setAttribute('hidden', 'true');
    });
  });
}

function initSearchSuggestions() {
  // already handled in initSearch; placeholder for future extension
}

function initTooltipPointer() {
  document.querySelectorAll('[data-tooltip]').forEach((tooltip) => {
    tooltip.addEventListener('pointerdown', () => {
      tooltip.setAttribute('aria-expanded', 'true');
    });
  });
}

function initPage() {
  initCopyButtons();
  initAudioPlayers();
  initContactForm();
  initCookieBanner();
  initDatePickers();
  initDropdowns();
  initDropdownAccessibility();
  initDropdownEscape();
  initFileUploader();
  initCarousel();
  initInputHelpers();
  initMiniCart();
  initModals();
  initWizard();
  initNewsletterForms();
  initNotificationBanner();
  initPopovers();
  initReviewForms();
  initReviewStars();
  initSearch();
  initSearchFormSubmission();
  initSearchSuggestionsRole();
  initSearchPrefill();
  initShareButtons();
  initShareFallbacks();
  initTableOfContents();
  initToast();
  initToastRegion();
  initTooltip();
  initTooltipAria();
  initTooltipPointer();
}

document.addEventListener('DOMContentLoaded', initPage);
