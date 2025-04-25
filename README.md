# Custom Search Engine (Google API + Flask)

A simple web-based search engine built with Flask, using the Google Custom Search API. It supports content safety filtering for sensitive keywords and highlights flagged results.

## Features
- Google Custom Search API integration
- Simple, Google-like UI (Chinese)
- Content safety: highlights results containing sensitive words
- Pagination (up to 5 pages)

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Get your [Google Custom Search API key](https://developers.google.com/custom-search/v1/overview) and Search Engine ID (CX).
4. Create a `.env` file in the project root with:
   ```env
   GOOGLE_API=your_google_api_key
   CX=your_search_engine_id
   ```

## Usage
Run the Flask app:
```bash
python app.py
```
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Project Structure
- `app.py` - Main Flask application
- `templates/` - HTML templates
- `tools/` - Helper scripts
- `test/` - Test scripts

## Notes
- The sensitive word list is in `app.py` (`badwords`).
- This project is for educational/demo purposes. Use your own API key and CX.
