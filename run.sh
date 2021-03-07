MV_MSG='missing variable:'

if [ "$BIN_VENV" == "" ]; then
  echo "$MV_MSG BIN_VENV"
  exit 1
fi

. $BIN_VENV/bin/activate

# THESE VARIABLES SHOULD BE SET IN THE VIRTUAL ENVIRONMENT ACTIVATE SCRIPT
if [ "$ACCOUNT_SID" == "" ]; then
  echo "$MV_MSG ACCOUNT_SID"
  deactivate
  exit 1
fi

if [ "$AUTH_TOKEN" == "" ]; then
  echo "$MV_MSG AUTH_TOKEN"
  deactivate
  exit 1
fi

if [ "$NUMBER" == "" ]; then
  echo "$MV_MSG NUMBER"
  deactivate
  exit 1
fi

if [ "$DELAY_IN_DAYS" == "" ]; then
  echo "$MV_MSG DELAY_IN_DAYS"
  deactivate
  exit 1
fi

if [ "$DB_ADDRESS" == "" ]; then
  echo "$MV_MSG DB_ADDRESS"
  deactivate
  exit 1
fi

export PYTHONPATH=src:$PYTHONPATH
pip3 install -r requirements.txt
python3 src/main.py $1
deactivate
