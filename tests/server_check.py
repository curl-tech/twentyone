import yaml

import sys
sys.path.append("src")

from server.app import app

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')