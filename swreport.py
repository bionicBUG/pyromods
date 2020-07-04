"""
Pyrobud module to report a message to spamwat.ch
Author : Ojas Sinha<sinhaojas67@gmail.com>
"""

import asyncio

from pyrobud import command, module, util

class SpamWatchReport(module.Module):
    name: str = "spamwat.ch reporter"
    disabled: bool = False

    @command.desc("Reports replied message to https://t.me/SpamWatchSupport")
    @command.alias("sw")
    @command.usage("[reply to a spam message]", reply=True)
    async def cmd_spamr(self, ctx: command.Context):
        group: str = "t.me/SpamWatchSupport"
        if (ctx.msg.is_reply or ctx.msg.file):
            spam = ctx.msg if ctx.msg.file else await ctx.msg.get_reply_message()
            await ctx.respond("__Reporting message to SpamWatch__")

            lines = []

            sender = await spam.get_sender()

            if sender:
                lines.append(f"Message author ID: `{sender.id}`")

            if spam.forward:
                if spam.forward.from_id:
                    lines.append(f"Forwarded message author ID: `{spam.forward.from_id}`")

            msg_data = "\n".join(lines)
            
            await self.bot.client.forward_messages(entity=group, messages=spam, silent=True)
            await self.bot.client.send_message(group, msg_data)

            await ctx.respond("__Reported to SpamWatch__")

        else:
            ctx.respond("__Reply to a message to report!__")
