from goplus.token import Token
from model.TokenHoldingSecurityData import TokenHoldingSecurityData
import time

def append_goplus_data(tokens: list[TokenHoldingSecurityData]):

    MAX_RETRIES = 4
    RETRY_DELAY = 15  # seconds
    done = 0

    for token in tokens:
        attempt = 0
        print(done)
        while attempt < MAX_RETRIES:
            try:
                data = Token(access_token=None).token_security(
                    chain_id="1",
                    addresses=[token.ca]
                )

                # Break early if valid response with result
                if data and hasattr(data, "result") and data.result:
                    result_data = data.result
                    goplus_security_data = list(result_data.values())[0] if result_data else {}
                    # print(goplus_security_data)
                    if goplus_security_data:
                        token.append_goplus_security_data(goplus_security_data)
                    print("Success", attempt)
                    done += 1
                    break

                print(f"Empty response for {token.ca}, retrying... ({attempt + 1}/{MAX_RETRIES})")
                attempt += 1
                time.sleep(RETRY_DELAY)

            except Exception as e:
                print(f"Error on attempt {attempt + 1} for {token.ca}: {e}")
                attempt += 1
                time.sleep(RETRY_DELAY)
