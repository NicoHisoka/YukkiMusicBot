import os
import aiohttp
import aiofiles

from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"): 
        return f"cache/{videoid}.png"

    url = f"https://techzbotsapi.herokuapp.com/thumb?videoid={videoid}&botname={MUSIC_BOT_NAME}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open( f"cache/thumb{videoid}.png", mode="wb" ) 
                    await f.write(await resp.read()) 
                    await f.close()

        return image_url        
    except Exception:
        return YOUTUBE_IMG_URL
