PYTHONPATH=src:$PYTHONPATH

MV_MSG='missing variable:'

if [ "$ACCOUNT_SID" == "" ]; then
  echo "$MV_MSG ACCOUNT_SID"
  exit 1
fi

if [ "$AUTH_TOKEN" == "" ]; then
  echo "$MV_MSG AUTH_TOKEN"
  exit 1
fi

if [ "$NUMBER" == "" ]; then
  echo "$MV_MSG NUMBER"
  exit 1
fi

if [ "$DELAY_IN_DAYS" == "" ]; then
  echo "$MV_MSG DELAY_IN_DAYS"
  exit 1
fi

if [ "$DB_ADDRESS" == "" ]; then
  echo "$MV_MSG DB_ADDRESS"
  exit 1
fi

python3 src/main.py $1
