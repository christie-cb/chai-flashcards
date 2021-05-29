from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py import share_bot, set_auth
from bot import Bot

DEVELOPER_UID =  # Fill these in using the values from https://chai.ml/dev
DEVELOPER_KEY =  # Fill these in using the values from https://chai.ml/dev

if DEVELOPER_KEY is None or DEVELOPER_UID is None:
    raise RuntimeError("Please fetch your UID and KEY from the bottom of the Chai Developer Platform. https://chai.ml/dev")

set_auth(DEVELOPER_UID, DEVELOPER_KEY)

BOT_IMAGE_URL = "https://images.unsplash.com/photo-1566039263025-caf125cd0994?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"

package(
    Metadata(
        name="CLRS Flashcards 🧠🤑💯",
        image_url=BOT_IMAGE_URL,
        color="f1a2b3",
        description="'The secret to getting ahead is getting started.' – Mark Twain.",
        input_class=Bot,
     ),
    requirements=["supermemo2"],
)

bot_uid = upload_and_deploy(
    "_package.zip"
)

wait_for_deployment(bot_uid)
share_bot(bot_uid)
