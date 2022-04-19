# Testing

All the tests, except `info()`, use cached responses for mocking tests, so tests will run quickly and not require credentials.

To test the `info()` function you'll need to set the `CARDTRADER_ACCESS_TOKEN` environment variable before running the tests.

If your code adds a new request to the cache, set the `CARDTRADER_ACCESS_TOKEN` environment variable before running the test, and it will be populated in `tests/cache.sqlite`.

At any point should you need to delete the database or repopulate it.
Set any credentials, and run the full test suite to repopulate it *(though some results might be different if any of the data has changed at CardTrader)*.
