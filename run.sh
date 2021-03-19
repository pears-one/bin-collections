USAGE='./$0 [live] [DELAY_IN_DAYS]'

function check_variable {
  var_name=$1
  var_value=${!var_name}
  MV_MSG='missing variable:'
  if [ "$var_value" == "" ]; then
    echo "$MV_MSG $var_name"
    deactivate 2> /dev/null
    exit 1
  fi
}

function is_int {
  [[ $# -ne 1 || $1 =~ [0-9]+ ]] && return
}

function is_live {
  [[ $1 == "live" ]] && return
}

function process_arguments {
  case $# in
    2)
      if is_int $2; then
        DELAY_IN_DAYS=$2
      fi
      if is_live $1; then
        MODE="live"
      fi
      ;;
    1)
      if is_int $1; then
        DELAY_IN_DAYS=$1
        return
      fi
      if is_live $1; then
        MODE="live"
      fi
    ;;
  esac
}

check_variable BIN_VENV

. $BIN_VENV/bin/activate

# THESE VARIABLES SHOULD BE SET IN THE VIRTUAL ENVIRONMENT ACTIVATE SCRIPT
check_variable ACCOUNT_SID
check_variable AUTH_TOKEN
check_variable NUMBER
check_variable DELAY_IN_DAYS
check_variable DB_ADDRESS

MODE="dev"
process_arguments $@

./pull.sh

export PYTHONPATH=src:$PYTHONPATH
pip3 install -r requirements.txt > /dev/null
python3 src/main.py $MODE
deactivate
