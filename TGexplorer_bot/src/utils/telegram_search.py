from typing import List, Dict, Any
import httpx

API_URL = "https://api.telegram.org/bot/"

async def search_channels_and_groups(token: str, keyword: str) -> List[Dict[str, Any]]:
    url = API_URL.format(token=token) + "getUpdates"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        results = []
        for update in data.get("result", []):
            if "channel_post" in update:
                channel = update["channel_post"]
                if keyword.lower() in channel.get("title", "").lower() or keyword.lower() in channel.get("caption", "").lower():
                    results.append({
                        "id": channel["chat"]["id"],
                        "title": channel["chat"]["title"],
                        "description": channel.get("caption", ""),
                        "type": "channel"
                    })
            elif "message" in update:
                message = update["message"]
                if keyword.lower() in message.get("text", "").lower():
                    results.append({
                        "id": message["chat"]["id"],
                        "title": message["chat"]["title"],
                        "description": message.get("text", ""),
                        "type": "group"
                    })
        return results

async def search_multimedia_messages(token: str, keyword: str) -> List[Dict[str, Any]]:
    url = API_URL.format(token=token) + "getUpdates"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        multimedia_results = []
        for update in data.get("result", []):
            if "channel_post" in update:
                channel = update["channel_post"]
                if keyword.lower() in channel.get("caption", "").lower():
                    multimedia_results.append({
                        "id": channel["chat"]["id"],
                        "title": channel["chat"]["title"],
                        "media_type": "photo" if "photo" in channel else "video" if "video" in channel else "audio",
                        "caption": channel.get("caption", "")
                    })
            elif "message" in update:
                message = update["message"]
                if keyword.lower() in message.get("caption", "").lower() or keyword.lower() in message.get("text", "").lower():
                    multimedia_results.append({
                        "id": message["chat"]["id"],
                        "title": message["chat"]["title"],
                        "media_type": "photo" if "photo" in message else "video" if "video" in message else "audio",
                        "caption": message.get("caption", "")
                    })
        return multimedia_results