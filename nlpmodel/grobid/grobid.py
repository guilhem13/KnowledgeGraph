from grobid_client.grobid_client import GrobidClient
import sys
print(sys.path)

if __name__ == "__main__":
    client = GrobidClient(config_path="../config.json")
    client.process("processFulltextDocument", "test2.pdf", output="./result/", consolidate_citations=True, teiCoordinates=True, force=True)