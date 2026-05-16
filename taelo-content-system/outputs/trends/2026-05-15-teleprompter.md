# Teleprompter — Anthropic's Same-Day Switch (v4 — Nate Herk tight cut)

*Target run time: ~12 min at 150 wpm (~1,780 words). v4 = redundancies stripped, personas one-line each, outro tightened, Friday reset closer added. Em-dashes are in-line pauses. Paragraph breaks are sip-of-water moments. Read aloud once before recording.*

---

Last Tuesday, Anthropic walked out in front of every tech reporter in the world and announced — fifty percent more Claude for you. Headlines wrote themselves. SpaceX compute deal. Free upgrade. Anthropic is doing you a favor. But when I found out what they were doing behind our back, I could not believe what I was actually witnessing. On the same afternoon, they buried the opposite news on a help-center page no journalist reads. They cut your background Claude agents by up to forty times. That is not a typo. Forty. Times.

Why the hell do you have to care? If you've ever played with agents, looked into them, or you're already using them — this affects you, greatly. And sooner or later, you're going to be using agents. That's just where the industry is going.

Right now, on a twenty dollar Pro plan, you can spin up Claude reviewing your pull requests, OpenClaw running tasks while you sleep, anything that types "claude dash p" in a terminal — all of it pulling from the same subscription. After June 15th, all of it draws from a separate credit. Twenty dollars on Pro. A hundred on Max 5x. Two hundred on Max 20x. After that — full API rates. The five thousand dollars of effective API value people have been pulling out of a two hundred dollar Max plan? Gone. The agent loops on a twenty dollar Pro sub? Gone.

So here's what this really means. You have a one-month window — before they pull this — to test things out while usage is still effectively uncapped. Because if you've never had to play with API bills before, you really don't want to be the one covering it. Trust me, I lived through OpenClaw bill shock a few months ago. Once you're paying your own agent's API bill — it gets hard to sleep with auto-top-up turned on.

What Anthropic did was a weasel move. And I'm not the first person saying it. Theo Browne — T3 Code creator, whose own product Anthropic explicitly cited in their announcement — canceled his Anthropic plan and called it "an attack on open source." Matt Pocock, who sells a Claude Code course, said the announcement "sounds like a bonus, why it might not actually be a bonus." Neither put the two May 13th announcements side-by-side. I'm going to. Math, deception, three moves before June 15th.

Announcement one. Last Tuesday. Anthropic's official news page. "Higher usage limits for Claude." Up fifty percent through July 13th. SpaceX compute deal. Three hundred megawatts of new GPUs. 9to5Google, Business Standard, AndroidHeadlines, Pulse2 — all positive. "More Claude for everyone." This is the announcement everyone saw.

Announcement two. Same afternoon. Help center page. Posted by ClaudeDevs, not the main Anthropic handle. "Use the Claude Agent SDK with your Claude plan." Opening line — "paid Claude plans can claim a dedicated monthly credit for programmatic usage." Sounds like a gift. It isn't. Starting June 15th, every Agent SDK call, every "claude dash p" script, every Claude Code GitHub Action, every third-party tool — capped at twenty dollars a month on Pro. No rollover.

One announcement makes the front page. The other gets a help-center URL. The second is the one that actually changes how much Claude you can run.

Now the math. Theo calculated that Max-plan users with Conductor or Zed or claude-dash-p in CI scripts had their usage cut by twenty-five to forty times. He didn't pull that number from thin air. The two hundred dollar Max 20x plan has been quoted as delivering up to five thousand dollars of effective API value every month. That's what indie hackers have been pulling out of it for a year. Starting June 15th, that same plan caps your programmatic usage at two hundred dollars. Five grand to two hundred. That's not a fifty percent change — that's a twenty-five times cut at the conservative end. Forty at the heavy end. On Sonnet-heavy workloads, the credible math goes as high as one hundred seventy-five times. The fifty percent increase headline that ran the same day? Different number, on purpose, pointed at a different audience.

And here's the part most people miss. The "Extra Usage" toggle — the thing that lets your subscription keep running past the credit cap — it is off by default. So a lot of people will hit the wall in late June without realizing it. Their agent silently dies mid-job at two a.m. on the eighteenth, and they find out the next morning when the PR review didn't ship.

Now the framing. Read the ClaudeDevs tweet — "we have heard your questions" is the language you use when you're delivering a feature people asked for. "Claim a dedicated monthly credit" — three words that frame this as something you're being given. Not something being capped.

It got shameless. Anthropic's own Lydia Hallie — Claude Code team — posted a tweet trying to clarify the change and got Community Noted within hours. Community Notes require broad consensus. When the platform's own consensus system has to correct your dev-rel team about your own pricing change, the framing has already failed.

And notice the channels. The fifty-percent-increase went out from the main Anthropic handle and got blasted by the PR machine. The credit-pool change went out from ClaudeDevs, a smaller sub-account. The press never saw the help-center page. The headline writers wrote what they were handed. This isn't a leak or a stumble. This is the standard playbook every API-priced company runs when they need to take something away — headline the gift, footnote the cost. Anthropic ran both halves the same day in the same press cycle and almost nobody put them side-by-side.

Which one of these is you.

The OpenClaw operator on a twenty dollar Pro plan, wrapping OpenClaw around Claude Code — old ceiling two hundred dollars of API value, new ceiling twenty. That's the ten-x cut. You're hit hardest.

The "claude-dash-p" scripter with cron jobs and content pipelines — five to ten x cut. Painless to fix if you measure before June 15th.

The GitHub Actions PR reviewer — your Claude bot averages one to three dollars per PR. Twenty dollar credit covers seven to twenty PRs a month. After that, your bot stops, quietly, on the eighteenth.

The agentic SaaS founder with users hitting your account — three choices. Eat the cost, pass through, or gate behind a paid tier.

The international operator running Claude-powered client work out of Korea, Singapore, anywhere outside the US — your margin lives in the subscription-to-value gap. If you're on Pro, move to API key with budget alerts before someone else's bill becomes your problem.

Three moves before June 15th.

Move one. Measure. Right now, before you close this video, open the Anthropic console, click Usage, and bookmark the page. That bookmark is the difference between the operator who plans and the one who panics on June 14th at midnight. Filter by API key, separate interactive from programmatic. You cannot make a decision without your number.

Move two. Sort every workflow into three buckets. Bucket A — keep on credit, anything interactive plus light programmatic that fits under twenty bucks. Bucket B — move to API key, production workflows, anything that runs while you sleep, anything that bills a client. Get an API key today, set a budget alert. Bucket C — kill it. There's always one Claude script you wrote three months ago that nobody is using. Stop paying for it.

Move three. If you use any third-party tool on the Agent SDK, send the vendor one email today. Ask one question. "What's your pricing model post-June 15th — are you eating the cost, passing through, or moving to a metered tier?" The ones that don't reply within seven days — migrate off.

Zoom out. This isn't a one-off. April 4th — Anthropic banned third-party agents. April 21st — they briefly removed Claude Code from Pro entirely, walked it back after outrage. May 13th — the credit split. Three subscription changes in six weeks. Each one took something from the power-user lane.

My take. Part one — the cut itself is defensible. The era of squeezing five grand of API value out of a two hundred dollar plan was always going to end. That was arbitrage. Anthropic isn't wrong to fix it.

Part two — the way they fixed it is not. Bury the bad news on a help page the day the good news hits the press. Frame the cut as a credit. Use "we heard your questions" language for a takeaway. Let your own dev-rel person get Community Noted. This isn't a billing change. This is a marketing strategy. They bet you'd see the headline and miss the help page. Don't.

Now here's the funny part. Two days after the announcement — last Friday — Anthropic suddenly reset everyone's five-hour and weekly counters. Every Pro, Max, Team, Enterprise subscriber, full quotas restored. A one-off goodwill gesture out of nowhere. Why? Because they're hearing the sentiment. Their own Claude Code PM Noah Zweben got replies calling the policy "gaslighting" and threats to switch to Codex. Meanwhile OpenAI is courting the same agent users with no AFK-versus-interactive split. Axios headline this week — "Anthropic tightens Claude limits as OpenAI courts agent users." That's not a coincidence. That's the market correcting in real time.

Comment which persona you are — top vote becomes the deep-dive next month. Like, subscribe, Claude for Small Business breakdown drops next week. See you.

(end — hold for 2 sec then cut)
