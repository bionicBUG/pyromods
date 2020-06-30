"""
A pyrobud module to download a file to the host.
Author : Ojas Sinha<sinhaojas67@gmail.com
""">

from io import BytesIO
from pathlib import Path
from pyrobud import command, module, util

class Download(module.Module):
    name: str="Download"
    disabled: bool= False

    @command.desc("Downloads the replied file on the host machine.")
    @command.alias("dw")
    @command.usage("Reply to a media to download", reply=True)
    async def cmd_download(self, ctx: command.Context):
        if not ctx.msg.is_reply:
            return "__Reply to a file to upload it.__"

        reply_msg = await ctx.msg.get_reply_message()
        if not reply_msg.file:
            return "__That message doesn't contain a file.__"


        ctx.respond("Starting download")
        data = await util.tg.download_file(ctx, reply_msg)

        buffer = BytesIO(data)
        buffer_name = reply_msg.file.name
        
        pathlib.Path(buffer_name).write_bytes(buffer.getbuffer())
