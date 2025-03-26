import requests
from bs4 import BeautifulSoup as soup
from model.TokenHoldingSecurityData import TokenHoldingSecurityData



def scrape_tokens() -> list[TokenHoldingSecurityData]:
    tokens: list[TokenHoldingSecurityData] = []
    token_address = "0x5be9a4959308a0d0c7bc0870e319314d8d957dbb"
    cur_link = f"https://etherscan.io/address/{token_address}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }
    page = requests.get(cur_link, headers=headers)
    page_content = soup(page.content, 'html5lib')

    lis = page_content.find_all('li', attrs={'class': 'list-custom-ERC20'})

    for li in lis:
        # Extract token name and ticker
        token_name_ticker = li.find('span', attrs={'data-bs-title': True})['data-bs-title']
        token_name, ticker = token_name_ticker.split(' (')
        ticker = ticker.strip(')')
        try:
            # Extract token amount (remove commas before conversion)
            amount_text = li.find('span', class_='text-muted').get_text(strip=True)
            # print("amount_text:", amount_text)

            try:
                amount_held = float(amount_text.split(' ')[0].replace(',', ''))
            except ValueError:
                amount_held = 0  # Default to 0 if parsing fails

            # Extract total value (handle missing cases)
            total_value_element = li.find('div', class_='list-usd-value')
            total_value_text = total_value_element.get_text(strip=True) if total_value_element else "Unknown total value"
            # print("total_value_text:", total_value_text)

            total_value = 0
            if total_value_text and total_value_text != "Unknown total value":
                try:
                    total_value = float(total_value_text.replace('$', '').replace(',', ''))
                except ValueError:
                    total_value = 0  # Default to 0 if parsing fails

            # Extract token price (handle missing cases)
            token_price_element = li.find('div', class_='list-usd-rate')
            token_price_text = token_price_element.get_text(strip=True) if token_price_element else "Unknown price"
            # print("token_price_text:", token_price_text)

            token_price = 0
            if token_price_text and token_price_text.startswith('@'):
                try:
                    token_price = float(token_price_text.replace('@', '').replace(',', '').strip())
                except ValueError:
                    token_price = 0  # Default to 0 if parsing fails

            token_contract_address = ""
            token_link_a = li.find('a', class_='nav-link')
            if token_link_a:
                token_link_href = token_link_a['href']
                if token_link_href:
                    try:
                        token_contract_address = token_link_href.split('/token/')[1].split('?')[0]
                    except ValueError:
                        token_contract_address = ""

            token = TokenHoldingSecurityData(
                name=token_name,
                ticker=ticker,
                amount=amount_held,
                price=token_price,
                total_value=total_value,
                ca=token_contract_address
            )
            tokens.append(token)

        except Exception as e:
            print(f"Error occured in '{ticker}' ", e)

    tokens.sort(key=lambda t: t.total_value, reverse=True)
    return tokens