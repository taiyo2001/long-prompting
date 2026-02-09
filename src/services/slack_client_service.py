import os
import logging
from typing import Any, Dict
from typing_extensions import Optional
from slack_sdk import WebClient

logger = logging.getLogger(__name__)

def build_image_generation_start_message(model_name: str, nodel_info: Dict[str, Any]) -> str:
    details = "\n".join([f"• *{k}*: `{v}`" for k, v in nodel_info.items()])
    return (
        f":art: モデル *{model_name}* の画像生成プロセスが開始されました！\n"
        f"詳細設定:\n{details}"
    )

def build_image_generation_complete_message(model_name: str) -> str:
    return f":white_check_mark: モデル *{model_name}* の画像生成プロセスが完了しました！"

def build_eval_start_message(model_name: str, dataset_name: str) -> str:
    return f":rocket: モデル *{model_name}* の評価が、データセット *{dataset_name}* で開始されました！"

def build_eval_complete_message(model_name: str, dataset_name: str) -> str:
    return f":white_check_mark: モデル *{model_name}* の評価が、データセット *{dataset_name}* で完了しました！"


class SlackService:
    def __init__(self):
        self.token = os.environ.get("SLACK_BOT_TOKEN")
        self.channel_id = os.environ.get("SLACK_CHANNEL_ID")
        self.client = WebClient(token=self.token)
        self.main_thread_ts = None
        WebClient

    def send_message(self, message: str, mention_id: Optional[str] = None, thread_ts: Optional[str] = None) -> bool:
        try:
            formatted_message = f"<@{mention_id}>\n{message}" if mention_id else message

            response = self.client.chat_postMessage(
                channel=self.channel_id,
                text=formatted_message,
                thread_ts=thread_ts
            )

            if response["ok"]:
                return response["ts"]
            return None

        except Exception as e:
            logger.error(f"Slack送信中に予期せぬエラーが発生しました: {e}")
            return False

slack_service = SlackService()
