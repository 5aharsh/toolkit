import requests, os, sys, time

class WGet:
    def download(self, link, name):
        '''
        Support function to download data
        '''
        file_name = name
        filled = u'\u2588'
        with open(file_name, "wb") as f:
            response = requests.get(link, stream=True)
            total_length = response.headers.get("content-length")
            print("Downloading %s from %s" % (file_name, link))
            print("Size: %s bytes" % (total_length))
            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write(
                        "\r[{filled}{empty}] {done:0.2f}%".format(
                            filled=filled * done, empty=" " * (50-done), done=(100*dl/total_length)
                        )
                    )
                    sys.stdout.flush()
            print("\nComplete!")
    
    def wget(self, link, name, retries):
        while retries:
            try:
                self.download(link, name)
            except requests.ConnectionError:
                retries-=1
                time.sleep(3)
                continue
            break