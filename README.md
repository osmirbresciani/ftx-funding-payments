<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python 3
- Pip

### Installation

1. Clone the repo
   ```
   git@github.com:osmirbresciani/ftx-exchange.git
   ```
2. Install requirements
   ```
   pip install -r requirements.txt
   ```
3. Rename `.env.example` to:
   ```
   .env
   ```
4. Enter your API_KEY and API_SECRET in `.env`
   ```
   API_KEY = " your API_KEY"
   API_SECRET = "your API_SECRET"
   SUBACCOUNT_NAME = "your SUBACCOUNT_NAME" [optional]
   ```
5. Set the markets that you wanna get the history of funding payments in `set_markets.py`

   ```
   markets = [
    "STEP-PERP",
    "BTC-PERP",
    "ETH-PERP",
    ]
   ```

   <!-- USAGE EXAMPLES -->

## Usage

1. In directory run:
   ```
   python3 main.py
   ```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.
