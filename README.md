# JOSAA Seat Allotment Scraper & Results Viewer

An interactive web-based tool to view and search JOSAA (Joint Seat Allocation Authority) seat allotment results.

**Live Demo:** [rkrrahman-786.github.io](https://rkrrahman-786.github.io)

---

## Features

- 🌐 **Interactive Web Interface** – Browse and search seat allotment results directly in the browser
- 📊 **Results Table** – Display allotment data (Institute, Program, Rank, Quota, etc.)
- 🔍 **Real-time Search & Filter** – Find seats by institute, program, category, quota, and more
- 📱 **Responsive Design** – Works seamlessly on desktop, tablet, and mobile devices
- 📈 **SEO Optimized** – Discoverable via Google Search with full meta tags, sitemap, and structured data

---

## Project Structure

```
.
├── index.html                    # Main web interface
├── styles.css                    # Styling
├── script.js                     # Frontend logic & interactivity
├── README.md                     # This file
├── render.yaml                   # Render deployment config
└── assets/                       # Images, logos, etc.
```

---

## Web Interface (GitHub Pages)

The web interface is hosted at **[rkrrahman-786.github.io](https://rkrrahman-786.github.io)** and provides:

1. **Search & Filter** – Find allotment results by round, institute, program, category, quota, etc.
2. **Table View** – Display results with sortable columns
3. **Responsive Design** – Works on desktop and mobile devices

### Accessing the Web Interface

Simply visit: **https://rkrrahman-786.github.io**

No setup required – it's a static web app deployed via Render.

---

## SEO & Search Engine Visibility

This site is fully optimized for Google Search and other search engines:

### What's Included

✅ **Meta Tags** – Title, description, keywords, author, robots directives  
✅ **Open Graph & Twitter Cards** – Social media preview optimization  
✅ **Sitemap** (`sitemap.xml`) – Tells Google what pages to index  
✅ **Robots.txt** – Guides crawler behavior and points to sitemap  
✅ **Structured Data** (`schema.org`) – Rich snippets for better SERP appearance  
✅ **Canonical URL** – Prevents duplicate content issues  
✅ **Mobile-Friendly** – Responsive design for all devices  
✅ **Fast Load Times** – Static site hosting on Render (CDN-backed)

### Indexing Status

- **Google Search Console:** Submit `https://rkrrahman-786.github.io/sitemap.xml`
- **Bing Webmaster Tools:** Add site for indexing
- **Search Time:** Usually indexed within 24-48 hours after first Google crawl

### Keywords Targeted

- JOSAA seat allotment
- IIT NIT results
- Engineering college admissions
- IIEST IIIT seats
- India engineering cutoff

---

## GitHub Pages & Render Configuration

The repository is configured for deployment on **Render.com** as a static site:

- **Repository:** `rkrrahman-786/rkrrahman-786.github.io`
- **Branch:** `main`
- **URL:** `https://rkrrahman-786.github.io` (with custom domain)
- **Platform:** [Render.com](https://render.com) – static site hosting

### Files

- **`render.yaml`** – Render deployment configuration (no build command needed)
- **`_config.yml`** – Site metadata and configuration
- **`index.html`** – Main page (served as static HTML)
- **`README.md`** – Documentation

### Deployment

1. **Connect your GitHub repo to Render:**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Static Site"
   - Select your GitHub repository: `rkrrahman-786/rkrrahman-786.github.io`
   - Set **Branch:** `main`
   - Set **Publish Directory:** `./` (root)
   - Leave **Build Command:** empty (no build needed for static HTML)
   - Click "Deploy"

2. **Auto-deploy on push:**
   - Every commit to the `main` branch automatically triggers a deploy
   - Site updates within 1-2 minutes

3. **Custom domain (optional):**
   - In Render dashboard, go to your static site
   - Settings → Custom Domain → Add `rkrrahman-786.github.io`
   - Update DNS records as instructed by Render

### Render Dashboard Link

[View your site on Render](https://dashboard.render.com)

---

## Technologies Used

### Frontend
- **HTML5** – Structure
- **CSS3** – Styling & responsive layout
- **Vanilla JavaScript** – Search, filtering, table rendering

### Hosting
- **Render.com** – Static site hosting (free tier available)

---

## Contributing

To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## Legal & Disclaimer

This tool is for **educational and informational purposes only**. Users are responsible for:

- Complying with the JOSAA portal's Terms of Service and robots.txt
- Respecting rate limits and server load
- Using scraped data responsibly and in accordance with applicable laws

The authors are not affiliated with JOSAA or the Indian government. Use at your own risk.

---

## License

This project is open source and available under the **MIT License** – see the LICENSE file for details.

---

## Support & Feedback

- **GitHub Issues:** [Report bugs or request features](https://github.com/rkrrahman-786/eduaakaashaa/issues)
- **Discussions:** [Ask questions or share ideas](https://github.com/rkrrahman-786/eduaakaashaa/discussions)

---

## Author

**rkrrahman-786**  
GitHub: [@rkrrahman-786](https://github.com/rkrrahman-786)

---

## Changelog

### v1.0.0 (Current)
- ✅ Interactive web interface for browsing seat allotment results
- ✅ Real-time search and filtering
- ✅ Responsive design (mobile-friendly)
- ✅ Render.com deployment

---

**Last Updated:** December 2025