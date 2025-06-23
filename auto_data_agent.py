<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Source Code | 7hNP4 | Rocket Powered Pastebin</title>
    <meta name="author" content="Sergio Benitez" />
    <meta http-equiv="Content-Security-Policy" content="
      default-src 'self';
      font-src data:;
      style-src-attr 'unsafe-inline';
      script-src 'none'
    ">
    <meta name="description" content="a simple, no-frills, command-line driven
      pastebin service powered by the Rocket web framework.">
    <link href="https:&#x2F;&#x2F;paste.rs/7hNP4" rel="canonical">
    <link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
    <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/normalize.min.css">
    <link rel="stylesheet" href="/code.min.css">
  </head>
  <body>
    <main>
      <div class="code gutter">
        <pre><span>1&#10;</span><span>2&#10;</span><span>3&#10;</span><span>4&#10;</span><span>5&#10;</span><span>6&#10;</span><span>7&#10;</span><span>8&#10;</span><span>9&#10;</span><span>10&#10;</span><span>11&#10;</span><span>12&#10;</span><span>13&#10;</span><span>14&#10;</span><span>15&#10;</span><span>16&#10;</span><span>17&#10;</span><span>18&#10;</span><span>19&#10;</span><span>20&#10;</span><span>21&#10;</span><span>22&#10;</span><span>23&#10;</span><span>24&#10;</span><span>25&#10;</span><span>26&#10;</span><span>27&#10;</span><span>28&#10;</span><span>29&#10;</span><span>30&#10;</span><span>31&#10;</span><span>32&#10;</span><span>33&#10;</span><span>34&#10;</span><span>35&#10;</span><span>36&#10;</span><span>37&#10;</span><span>38&#10;</span><span>39&#10;</span><span>40&#10;</span><span>41&#10;</span><span>42&#10;</span><span>43&#10;</span><span>44&#10;</span><span>45&#10;</span><span>46&#10;</span><span>47&#10;</span><span>48&#10;</span><span>49&#10;</span><span>50&#10;</span><span>51&#10;</span><span>52&#10;</span><span>53&#10;</span><span>54&#10;</span><span>55&#10;</span><span>56&#10;</span><span>57&#10;</span><span>58&#10;</span><span>59&#10;</span><span>60&#10;</span><span>61&#10;</span><span>62&#10;</span><span>63&#10;</span><span>64&#10;</span><span>65&#10;</span><span>66&#10;</span><span>67&#10;</span><span>68&#10;</span><span>69&#10;</span><span>70&#10;</span><span>71&#10;</span><span>72&#10;</span><span>73&#10;</span><span>74&#10;</span><span>75&#10;</span><span>76&#10;</span><span>77&#10;</span><span>78&#10;</span><span>79&#10;</span><span>80&#10;</span><span>81&#10;</span><span>82&#10;</span><span>83&#10;</span><span>84&#10;</span><span>85&#10;</span><span>86&#10;</span><span>87&#10;</span><span>88&#10;</span><span>89&#10;</span><span>90&#10;</span><span>91&#10;</span><span>92&#10;</span><span>93&#10;</span><span>94&#10;</span><span>95&#10;</span><span>96&#10;</span><span>97&#10;</span><span>98&#10;</span><span>99&#10;</span><span>100&#10;</span><span>101&#10;</span><span>102&#10;</span><span>103&#10;</span><span>104&#10;</span><span>105&#10;</span><span>106&#10;</span><span>107&#10;</span><span>108&#10;</span><span>109&#10;</span><span>110&#10;</span><span>111&#10;</span><span>112&#10;</span><span>113&#10;</span><span>114&#10;</span><span>115&#10;</span><span>116&#10;</span><span>117&#10;</span><span>118&#10;</span><span>119&#10;</span><span>120&#10;</span><span>121&#10;</span><span>122&#10;</span><span>123&#10;</span><span>124&#10;</span><span>125&#10;</span><span>126&#10;</span><span>127&#10;</span><span>128&#10;</span><span>129&#10;</span><span>130&#10;</span><span>131&#10;</span><span>132&#10;</span><span>133&#10;</span><span>134&#10;</span><span>135&#10;</span><span>136&#10;</span><span>137&#10;</span><span>138&#10;</span><span>139&#10;</span><span>140&#10;</span><span>141&#10;</span><span>142&#10;</span><span>143&#10;</span><span>144&#10;</span><span>145&#10;</span><span>146&#10;</span><span>147&#10;</span><span>148&#10;</span><span>149&#10;</span><span>150&#10;</span><span>151&#10;</span><span>152&#10;</span><span>153&#10;</span><span>154&#10;</span><span>155&#10;</span><span>156&#10;</span><span>157&#10;</span><span>158&#10;</span><span>159&#10;</span><span>160&#10;</span><span>161&#10;</span><span>162&#10;</span><span>163&#10;</span><span>164&#10;</span><span>165&#10;</span><span>166&#10;</span><span>167&#10;</span><span>168&#10;</span><span>169&#10;</span><span>170&#10;</span><span>171&#10;</span><span>172&#10;</span><span>173&#10;</span><span>174&#10;</span><span>175&#10;</span><span>176&#10;</span><span>177&#10;</span><span>178&#10;</span><span>179&#10;</span><span>180&#10;</span><span>181&#10;</span><span>182&#10;</span><span>183&#10;</span><span>184&#10;</span><span>185&#10;</span><span>186&#10;</span><span>187&#10;</span><span>188&#10;</span><span>189&#10;</span><span>190&#10;</span><span>191&#10;</span><span>192&#10;</span><span>193&#10;</span><span>194&#10;</span><span>195&#10;</span><span>196&#10;</span><span>197&#10;</span><span>198&#10;</span><span>199&#10;</span><span>200&#10;</span><span>201&#10;</span><span>202&#10;</span><span>203&#10;</span><span>204&#10;</span><span>205&#10;</span><span>206&#10;</span><span>207&#10;</span><span>208&#10;</span><span>209&#10;</span><span>210&#10;</span><span>211&#10;</span><span>212&#10;</span><span>213&#10;</span><span>214&#10;</span><span>215&#10;</span><span>216&#10;</span><span>217&#10;</span><span>218&#10;</span><span>219&#10;</span><span>220&#10;</span><span>221&#10;</span><span>222&#10;</span><span>223&#10;</span><span>224&#10;</span><span>225&#10;</span><span>226&#10;</span><span>227&#10;</span><span>228&#10;</span><span>229&#10;</span><span>230&#10;</span><span>231&#10;</span><span>232&#10;</span><span>233&#10;</span><span>234&#10;</span><span>235&#10;</span><span>236&#10;</span><span>237&#10;</span><span>238&#10;</span><span>239&#10;</span><span>240&#10;</span><span>241&#10;</span><span>242&#10;</span><span>243&#10;</span><span>244&#10;</span><span>245&#10;</span><span>246&#10;</span><span>247&#10;</span><span>248&#10;</span><span>249&#10;</span><span>250&#10;</span><span>251&#10;</span><span>252&#10;</span><span>253&#10;</span><span>254&#10;</span><span>255&#10;</span><span>256&#10;</span><span>257&#10;</span><span>258&#10;</span><span>259&#10;</span><span>260&#10;</span><span>261&#10;</span><span>262&#10;</span><span>263&#10;</span><span>264&#10;</span><span>265&#10;</span><span>266&#10;</span><span>267&#10;</span><span>268&#10;</span><span>269&#10;</span><span>270&#10;</span><span>271&#10;</span><span>272&#10;</span><span>273&#10;</span><span>274&#10;</span><span>275&#10;</span><span>276&#10;</span><span>277&#10;</span><span>278&#10;</span><span>279&#10;</span><span>280&#10;</span><span>281&#10;</span><span>282&#10;</span><span>283&#10;</span><span>284&#10;</span><span>285&#10;</span><span>286&#10;</span><span>287&#10;</span><span>288&#10;</span><span>289&#10;</span><span>290&#10;</span><span>291&#10;</span><span>292&#10;</span><span>293&#10;</span></pre>
      </div>
      <div class="code text">
          <pre style="background-color:#ffffff;">
<span style="font-style:italic;color:#969896;">#!/usr/bin/env python3
</span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;
</span><span style="font-style:italic;color:#969896;">auto_data_agent.py
</span><span style="font-style:italic;color:#969896;">~~~~~~~~~~~~~~~~~~
</span><span style="font-style:italic;color:#969896;">
</span><span style="font-style:italic;color:#969896;">Automated data‑agent voor budget/ startersauto‑advertenties.
</span><span style="font-style:italic;color:#969896;">
</span><span style="font-style:italic;color:#969896;">– Scraped platforms: Marktplaats, Facebook Marketplace, AutoScout24, mobile.de,
</span><span style="font-style:italic;color:#969896;">  eBay Kleinanzeigen, Amazon (auto‑categorie), Schadeautos.nl
</span><span style="font-style:italic;color:#969896;">– Verrijkt elke advertentie met dagwaarde (ANWB/ Autotelex/ vergelijkbare prijzen)
</span><span style="font-style:italic;color:#969896;">– Bewaart alleen aanbiedingen onder dagwaarde
</span><span style="font-style:italic;color:#969896;">– Exporteert resultaat naar Excel (.xlsx) met unieke bestandsnaam
</span><span style="font-style:italic;color:#969896;">– Logt elke run (timestamp, aantallen, errors)
</span><span style="font-style:italic;color:#969896;">– Kan optioneel een webhook/ e‑mail sturen bij nieuwe hits
</span><span style="font-style:italic;color:#969896;">– Ontworpen om iedere 3 uur via cron of `schedule` te draaien
</span><span style="font-style:italic;color:#969896;">
</span><span style="font-style:italic;color:#969896;">Alle belangrijke instellingen staan bovenin dit bestand.
</span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">from </span><span style="color:#323232;">__future__ </span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">annotations
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">os
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">sys
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">json
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">time
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">math
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">glob
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">uuid
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">queue
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">random
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">string
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">shutil
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">logging
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">datetime </span><span style="font-weight:bold;color:#a71d5d;">as </span><span style="color:#323232;">dt
</span><span style="font-weight:bold;color:#a71d5d;">from </span><span style="color:#323232;">dataclasses </span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">dataclass, asdict
</span><span style="font-weight:bold;color:#a71d5d;">from </span><span style="color:#323232;">typing </span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">List, Dict, Any, Callable
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">pandas </span><span style="font-weight:bold;color:#a71d5d;">as </span><span style="color:#323232;">pd
</span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">requests
</span><span style="font-weight:bold;color:#a71d5d;">from </span><span style="color:#323232;">bs4 </span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">BeautifulSoup
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># CONFIGURATIE (pas hier de filters/platforms eenvoudig aan)
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="color:#0086b3;">MODELLEN </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">[
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;Volkswagen Polo&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Toyota Aygo&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Ford Fiesta&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Kia Picanto&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;Renault Clio&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Seat Ibiza&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Peugeot 108&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Citroën C1&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;Opel Corsa&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Hyundai i10&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Peugeot 208&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Ford Focus&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;Volkswagen Golf&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Kia Rio&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Seat Leon&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Peugeot 207&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;Peugeot 206&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Fiat 500&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Mini&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Opel Astra&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;Renault Mégane&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Suzuki Swift&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;Volkswagen Up&quot;
</span><span style="color:#323232;">]
</span><span style="color:#0086b3;">MAX_BUDGET_EUR</span><span style="color:#323232;">: </span><span style="color:#0086b3;">int </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">7_500
</span><span style="color:#0086b3;">MIN_BOUWJAAR</span><span style="color:#323232;">: </span><span style="color:#0086b3;">int </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">2008
</span><span style="color:#0086b3;">MAX_KILOMETERS</span><span style="color:#323232;">: </span><span style="color:#0086b3;">int </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">160_000
</span><span style="color:#0086b3;">RUN_INTERVAL_HOURS</span><span style="color:#323232;">: </span><span style="color:#0086b3;">int </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">3
</span><span style="color:#323232;">
</span><span style="color:#0086b3;">PLATFORMS </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">[
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;marktplaats&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;autoscout24&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;mobile_de&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;ebay_kleinanzeigen&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;schadeautos&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;facebook_marketplace&quot;
</span><span style="color:#323232;">]
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># Optionele notificatie
</span><span style="color:#0086b3;">ENABLE_NOTIFICATION</span><span style="color:#323232;">: </span><span style="color:#0086b3;">bool </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">False
</span><span style="color:#0086b3;">WEBHOOK_URL</span><span style="color:#323232;">: </span><span style="color:#0086b3;">str </span><span style="font-weight:bold;color:#a71d5d;">| </span><span style="color:#0086b3;">None </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">None      </span><span style="font-style:italic;color:#969896;"># bv. Slack/Discord webhook
</span><span style="color:#0086b3;">EMAIL_SETTINGS</span><span style="color:#323232;">: Dict[</span><span style="color:#0086b3;">str</span><span style="color:#323232;">, </span><span style="color:#0086b3;">str</span><span style="color:#323232;">] </span><span style="font-weight:bold;color:#a71d5d;">| </span><span style="color:#0086b3;">None </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">None  </span><span style="font-style:italic;color:#969896;"># SMTP config
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># Padinstellingen
</span><span style="color:#0086b3;">BASE_DIR </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">abspath(os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">dirname(__file__))
</span><span style="color:#0086b3;">OUTPUT_DIR </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">join(</span><span style="color:#0086b3;">BASE_DIR</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;output&quot;</span><span style="color:#323232;">)
</span><span style="color:#0086b3;">LOG_DIR </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">join(</span><span style="color:#0086b3;">BASE_DIR</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;logs&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">makedirs(</span><span style="color:#0086b3;">OUTPUT_DIR</span><span style="color:#323232;">, exist_ok</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#0086b3;">True</span><span style="color:#323232;">)
</span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">makedirs(</span><span style="color:#0086b3;">LOG_DIR</span><span style="color:#323232;">, exist_ok</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#0086b3;">True</span><span style="color:#323232;">)
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># LOGGING
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="color:#323232;">timestamp </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">dt</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">datetime</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">now()</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">strftime(</span><span style="color:#183691;">&quot;</span><span style="color:#0086b3;">%Y%m%d</span><span style="color:#183691;">_</span><span style="color:#0086b3;">%H%M%S</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">log_file </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">join(</span><span style="color:#0086b3;">LOG_DIR</span><span style="color:#323232;">, </span><span style="font-weight:bold;color:#a71d5d;">f</span><span style="color:#183691;">&quot;run_</span><span style="color:#323232;">{timestamp}</span><span style="color:#183691;">.log&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">logging</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">basicConfig(
</span><span style="color:#323232;">    level</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#323232;">logging</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#0086b3;">INFO</span><span style="color:#323232;">,
</span><span style="color:#323232;">    format</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#183691;">&quot;</span><span style="color:#0086b3;">%(</span><span style="color:#323232;">asctime</span><span style="color:#0086b3;">)s</span><span style="color:#183691;">  [</span><span style="color:#0086b3;">%(</span><span style="color:#323232;">levelname</span><span style="color:#0086b3;">)s</span><span style="color:#183691;">]  </span><span style="color:#0086b3;">%(</span><span style="color:#323232;">message</span><span style="color:#0086b3;">)s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">    handlers</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#323232;">[
</span><span style="color:#323232;">        logging</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">FileHandler(log_file, encoding</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#183691;">&quot;utf-8&quot;</span><span style="color:#323232;">),
</span><span style="color:#323232;">        logging</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">StreamHandler(sys</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">stdout)
</span><span style="color:#323232;">    ],
</span><span style="color:#323232;">)
</span><span style="color:#323232;">logger </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">logging</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">getLogger(</span><span style="color:#183691;">&quot;auto_data_agent&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># DATACLASS DEFINITIE
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="color:#323232;">@dataclass
</span><span style="font-weight:bold;color:#a71d5d;">class </span><span style="color:#0086b3;">Ad</span><span style="color:#323232;">:
</span><span style="color:#323232;">    platform: </span><span style="color:#0086b3;">str
</span><span style="color:#323232;">    title: </span><span style="color:#0086b3;">str
</span><span style="color:#323232;">    model: </span><span style="color:#0086b3;">str
</span><span style="color:#323232;">    price: </span><span style="color:#0086b3;">float
</span><span style="color:#323232;">    day_value: </span><span style="color:#0086b3;">float
</span><span style="color:#323232;">    year: </span><span style="color:#0086b3;">int
</span><span style="color:#323232;">    km: </span><span style="color:#0086b3;">int
</span><span style="color:#323232;">    url: </span><span style="color:#0086b3;">str
</span><span style="color:#323232;">    location: </span><span style="color:#0086b3;">str </span><span style="font-weight:bold;color:#a71d5d;">| </span><span style="color:#0086b3;">None </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">None
</span><span style="color:#323232;">    extra: Dict[</span><span style="color:#0086b3;">str</span><span style="color:#323232;">, Any] </span><span style="font-weight:bold;color:#a71d5d;">| </span><span style="color:#0086b3;">None </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">None
</span><span style="color:#323232;">
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">to_dict</span><span style="color:#323232;">(self) -&gt; Dict[</span><span style="color:#0086b3;">str</span><span style="color:#323232;">, Any]:
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">asdict(self)
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># HULPFUNCTIES
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">fetch_url</span><span style="color:#323232;">(url: </span><span style="color:#0086b3;">str</span><span style="color:#323232;">, </span><span style="font-weight:bold;color:#a71d5d;">**</span><span style="color:#323232;">kwargs) -&gt; requests</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">Response </span><span style="font-weight:bold;color:#a71d5d;">| </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;Wrapper rond requests.get met eenvoudige foutafhandeling.&quot;&quot;&quot;
</span><span style="color:#323232;">    headers </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">kwargs</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">pop(
</span><span style="color:#323232;">        </span><span style="color:#183691;">&quot;headers&quot;</span><span style="color:#323232;">,
</span><span style="color:#323232;">        {
</span><span style="color:#323232;">            </span><span style="color:#183691;">&quot;User-Agent&quot;</span><span style="color:#323232;">: (
</span><span style="color:#323232;">                </span><span style="color:#183691;">&quot;Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 &quot;
</span><span style="color:#323232;">                </span><span style="color:#183691;">&quot;(KHTML, like Gecko) Chrome/122.0 Safari/537.36&quot;
</span><span style="color:#323232;">            )
</span><span style="color:#323232;">        },
</span><span style="color:#323232;">    )
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">try</span><span style="color:#323232;">:
</span><span style="color:#323232;">        resp </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">requests</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">get(url, headers</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#323232;">headers, timeout</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#0086b3;">15</span><span style="color:#323232;">, </span><span style="font-weight:bold;color:#a71d5d;">**</span><span style="color:#323232;">kwargs)
</span><span style="color:#323232;">        resp</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">raise_for_status()
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">resp
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">except </span><span style="color:#0086b3;">Exception </span><span style="font-weight:bold;color:#a71d5d;">as </span><span style="color:#323232;">exc:
</span><span style="color:#323232;">        logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">warning(</span><span style="color:#183691;">&quot;Fout bij ophalen </span><span style="color:#0086b3;">%s</span><span style="color:#183691;"> – </span><span style="color:#0086b3;">%s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, url, exc)
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#0086b3;">None
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">get_day_value</span><span style="color:#323232;">(model: </span><span style="color:#0086b3;">str</span><span style="color:#323232;">, year: </span><span style="color:#0086b3;">int</span><span style="color:#323232;">, km: </span><span style="color:#0086b3;">int</span><span style="color:#323232;">) -&gt; </span><span style="color:#0086b3;">float </span><span style="font-weight:bold;color:#a71d5d;">| </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;
</span><span style="font-style:italic;color:#969896;">    Dummy‑implementatie voor dagwaarde.
</span><span style="font-style:italic;color:#969896;">    – In productie: scrape ANWB Koerslijst of Autotelex API.
</span><span style="font-style:italic;color:#969896;">    – Hier gebruiken we een ruwe schatting (afschrijving 10%/jr, 0,02 €/km).
</span><span style="font-style:italic;color:#969896;">    &quot;&quot;&quot;
</span><span style="color:#323232;">    basis </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#0086b3;">20_000  </span><span style="font-style:italic;color:#969896;"># fictieve nieuwprijs
</span><span style="color:#323232;">    leeftijd </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#62a35c;">max</span><span style="color:#323232;">(</span><span style="color:#0086b3;">0</span><span style="color:#323232;">, dt</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">datetime</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">now()</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">year </span><span style="font-weight:bold;color:#a71d5d;">- </span><span style="color:#323232;">year)
</span><span style="color:#323232;">    waarde </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">basis </span><span style="font-weight:bold;color:#a71d5d;">* </span><span style="color:#323232;">(</span><span style="color:#0086b3;">0.90 </span><span style="font-weight:bold;color:#a71d5d;">** </span><span style="color:#323232;">leeftijd) </span><span style="font-weight:bold;color:#a71d5d;">- </span><span style="color:#323232;">(km </span><span style="font-weight:bold;color:#a71d5d;">* </span><span style="color:#0086b3;">0.02</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#62a35c;">round</span><span style="color:#323232;">(</span><span style="color:#62a35c;">max</span><span style="color:#323232;">(waarde, </span><span style="color:#0086b3;">500</span><span style="color:#323232;">), </span><span style="color:#0086b3;">2</span><span style="color:#323232;">)
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">price_below_dayvalue</span><span style="color:#323232;">(price: </span><span style="color:#0086b3;">float</span><span style="color:#323232;">, day_value: </span><span style="color:#0086b3;">float</span><span style="color:#323232;">) -&gt; </span><span style="color:#0086b3;">bool</span><span style="color:#323232;">:
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">price </span><span style="font-weight:bold;color:#a71d5d;">&lt; </span><span style="color:#323232;">day_value
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">unique_filename</span><span style="color:#323232;">(prefix: </span><span style="color:#0086b3;">str</span><span style="color:#323232;">, ext: </span><span style="color:#0086b3;">str </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#183691;">&quot;.xlsx&quot;</span><span style="color:#323232;">) -&gt; </span><span style="color:#0086b3;">str</span><span style="color:#323232;">:
</span><span style="color:#323232;">    ts </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">dt</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">datetime</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">now()</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">strftime(</span><span style="color:#183691;">&quot;</span><span style="color:#0086b3;">%Y%m%d</span><span style="color:#183691;">_</span><span style="color:#0086b3;">%H%M%S</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return f</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">{prefix}</span><span style="color:#183691;">_</span><span style="color:#323232;">{ts}{ext}</span><span style="color:#183691;">&quot;
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># SCRAPER PLACEHOLDERS
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">scrape_marktplaats</span><span style="color:#323232;">() -&gt; List[Ad]:
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;Voorbeeldscraper Marktplaats – vervang door echte implementatie.&quot;&quot;&quot;
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Scraping Marktplaats (placeholder)&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;"># … echte scraping‑code hier …
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">scrape_autoscout24</span><span style="color:#323232;">() -&gt; List[Ad]:
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Scraping AutoScout24 (placeholder)&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">scrape_mobile_de</span><span style="color:#323232;">() -&gt; List[Ad]:
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Scraping mobile.de (placeholder)&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">scrape_ebay_kleinanzeigen</span><span style="color:#323232;">() -&gt; List[Ad]:
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Scraping eBay Kleinanzeigen (placeholder)&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">scrape_schadeautos</span><span style="color:#323232;">() -&gt; List[Ad]:
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Scraping Schadeautos.nl (placeholder)&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">scrape_facebook_marketplace</span><span style="color:#323232;">() -&gt; List[Ad]:
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;
</span><span style="font-style:italic;color:#969896;">    Facebook Marketplace vereist inloggen &amp; mogelijk Selenium.
</span><span style="font-style:italic;color:#969896;">    Hier alleen placeholder – implementatie buiten scope.
</span><span style="font-style:italic;color:#969896;">    &quot;&quot;&quot;
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Scraping Facebook Marketplace (placeholder)&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">return </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="color:#0086b3;">SCRAPER_MAP</span><span style="color:#323232;">: Dict[</span><span style="color:#0086b3;">str</span><span style="color:#323232;">, Callable[[], List[Ad]]] </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">{
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;marktplaats&quot;</span><span style="color:#323232;">: scrape_marktplaats,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;autoscout24&quot;</span><span style="color:#323232;">: scrape_autoscout24,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;mobile_de&quot;</span><span style="color:#323232;">: scrape_mobile_de,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;ebay_kleinanzeigen&quot;</span><span style="color:#323232;">: scrape_ebay_kleinanzeigen,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;schadeautos&quot;</span><span style="color:#323232;">: scrape_schadeautos,
</span><span style="color:#323232;">    </span><span style="color:#183691;">&quot;facebook_marketplace&quot;</span><span style="color:#323232;">: scrape_facebook_marketplace,
</span><span style="color:#323232;">}
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># MAIN WORKFLOW
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">run_once</span><span style="color:#323232;">() -&gt; </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Start nieuwe run – platforms: </span><span style="color:#0086b3;">%s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, </span><span style="color:#183691;">&quot;, &quot;</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">join(</span><span style="color:#0086b3;">PLATFORMS</span><span style="color:#323232;">))
</span><span style="color:#323232;">    found_ads: List[Ad] </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">[]
</span><span style="color:#323232;">
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;"># 1) Scrapen
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">for </span><span style="color:#323232;">platform </span><span style="font-weight:bold;color:#a71d5d;">in </span><span style="color:#0086b3;">PLATFORMS</span><span style="color:#323232;">:
</span><span style="color:#323232;">        scraper </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">SCRAPER_MAP</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">get(platform)
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#323232;">scraper </span><span style="font-weight:bold;color:#a71d5d;">is </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">            logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">warning(</span><span style="color:#183691;">&quot;Geen scraper voor platform </span><span style="color:#0086b3;">%s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, platform)
</span><span style="color:#323232;">            </span><span style="font-weight:bold;color:#a71d5d;">continue
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">try</span><span style="color:#323232;">:
</span><span style="color:#323232;">            ads </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">scraper()
</span><span style="color:#323232;">            found_ads</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">extend(ads)
</span><span style="color:#323232;">            logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Platform </span><span style="color:#0086b3;">%s</span><span style="color:#183691;"> leverde </span><span style="color:#0086b3;">%d</span><span style="color:#183691;"> advertenties&quot;</span><span style="color:#323232;">, platform, </span><span style="color:#62a35c;">len</span><span style="color:#323232;">(ads))
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">except </span><span style="color:#0086b3;">Exception </span><span style="font-weight:bold;color:#a71d5d;">as </span><span style="color:#323232;">exc:
</span><span style="color:#323232;">            logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">exception(</span><span style="color:#183691;">&quot;Scraper </span><span style="color:#0086b3;">%s</span><span style="color:#183691;"> mislukte: </span><span style="color:#0086b3;">%s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, platform, exc)
</span><span style="color:#323232;">
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Totaal gevonden advertenties: </span><span style="color:#0086b3;">%d</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, </span><span style="color:#62a35c;">len</span><span style="color:#323232;">(found_ads))
</span><span style="color:#323232;">
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;"># 2) Verrijken &amp; filteren
</span><span style="color:#323232;">    selected_ads: List[Dict[</span><span style="color:#0086b3;">str</span><span style="color:#323232;">, Any]] </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">[]
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">for </span><span style="color:#323232;">ad </span><span style="font-weight:bold;color:#a71d5d;">in </span><span style="color:#323232;">found_ads:
</span><span style="color:#323232;">        day_val </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">day_value </span><span style="font-weight:bold;color:#a71d5d;">or </span><span style="color:#323232;">get_day_value(ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">model, ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">year, ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">km)
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#323232;">day_val </span><span style="font-weight:bold;color:#a71d5d;">is </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">            </span><span style="font-weight:bold;color:#a71d5d;">continue
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#323232;">price_below_dayvalue(ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">price, day_val):
</span><span style="color:#323232;">            ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">day_value </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">day_val
</span><span style="color:#323232;">            selected_ads</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">append(ad</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">to_dict())
</span><span style="color:#323232;">
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Advertenties onder dagwaarde: </span><span style="color:#0086b3;">%d</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, </span><span style="color:#62a35c;">len</span><span style="color:#323232;">(selected_ads))
</span><span style="color:#323232;">
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;"># 3) Exporteren
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#323232;">selected_ads:
</span><span style="color:#323232;">        df </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">pd</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">DataFrame(selected_ads)
</span><span style="color:#323232;">        fname </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">unique_filename(</span><span style="color:#183691;">&quot;auto_deals&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">        out_path </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">join(</span><span style="color:#0086b3;">OUTPUT_DIR</span><span style="color:#323232;">, fname)
</span><span style="color:#323232;">        df</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">to_excel(out_path, index</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#0086b3;">False</span><span style="color:#323232;">)
</span><span style="color:#323232;">        logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Resultaat opgeslagen in </span><span style="color:#0086b3;">%s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, out_path)
</span><span style="color:#323232;">
</span><span style="color:#323232;">        </span><span style="font-style:italic;color:#969896;"># 4) Notificatie
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#0086b3;">ENABLE_NOTIFICATION</span><span style="color:#323232;">:
</span><span style="color:#323232;">            </span><span style="font-weight:bold;color:#a71d5d;">try</span><span style="color:#323232;">:
</span><span style="color:#323232;">                send_notification(</span><span style="color:#62a35c;">len</span><span style="color:#323232;">(selected_ads), out_path)
</span><span style="color:#323232;">            </span><span style="font-weight:bold;color:#a71d5d;">except </span><span style="color:#0086b3;">Exception </span><span style="font-weight:bold;color:#a71d5d;">as </span><span style="color:#323232;">exc:
</span><span style="color:#323232;">                logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">warning(</span><span style="color:#183691;">&quot;Notificatie mislukte: </span><span style="color:#0086b3;">%s</span><span style="color:#183691;">&quot;</span><span style="color:#323232;">, exc)
</span><span style="color:#323232;">
</span><span style="color:#323232;">    logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Run afgerond&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># NOTIFICATIE (optioneel)
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">send_notification</span><span style="color:#323232;">(count: </span><span style="color:#0086b3;">int</span><span style="color:#323232;">, file_path: </span><span style="color:#0086b3;">str</span><span style="color:#323232;">) -&gt; </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#0086b3;">WEBHOOK_URL</span><span style="color:#323232;">:
</span><span style="color:#323232;">        msg </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">{
</span><span style="color:#323232;">            </span><span style="color:#183691;">&quot;text&quot;</span><span style="color:#323232;">: </span><span style="font-weight:bold;color:#a71d5d;">f</span><span style="color:#183691;">&quot;Nieuwe interessante auto‑advertenties gevonden: </span><span style="color:#323232;">{count}</span><span style="color:#0086b3;">\n</span><span style="color:#183691;">Bestand: </span><span style="color:#323232;">{os</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">path</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">basename(file_path)}</span><span style="color:#183691;">&quot;
</span><span style="color:#323232;">        }
</span><span style="color:#323232;">        resp </span><span style="font-weight:bold;color:#a71d5d;">= </span><span style="color:#323232;">requests</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">post(</span><span style="color:#0086b3;">WEBHOOK_URL</span><span style="color:#323232;">, json</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#323232;">msg, timeout</span><span style="font-weight:bold;color:#a71d5d;">=</span><span style="color:#0086b3;">10</span><span style="color:#323232;">)
</span><span style="color:#323232;">        resp</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">raise_for_status()
</span><span style="color:#323232;">        logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Webhook verstuurd (</span><span style="color:#0086b3;">%s</span><span style="color:#183691;">)&quot;</span><span style="color:#323232;">, resp</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">status_code)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">elif </span><span style="color:#0086b3;">EMAIL_SETTINGS</span><span style="color:#323232;">:
</span><span style="color:#323232;">        </span><span style="font-style:italic;color:#969896;"># Implementatie SMTP/ email indien gewenst
</span><span style="color:#323232;">        logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;E‑mailnotificatie nog niet geïmplementeerd&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">else</span><span style="color:#323232;">:
</span><span style="color:#323232;">        logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Geen notificatie‑methode geconfigureerd&quot;</span><span style="color:#323232;">)
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-style:italic;color:#969896;"># CLI
</span><span style="font-style:italic;color:#969896;"># ──────────────────────────────────────────────────────────────
</span><span style="font-weight:bold;color:#a71d5d;">def </span><span style="font-weight:bold;color:#323232;">main</span><span style="color:#323232;">() -&gt; </span><span style="color:#0086b3;">None</span><span style="color:#323232;">:
</span><span style="color:#323232;">    </span><span style="font-style:italic;color:#969896;">&quot;&quot;&quot;
</span><span style="font-style:italic;color:#969896;">    – Zonder argumenten: draait één keer (handmatig/ cron)
</span><span style="font-style:italic;color:#969896;">    – Met argument `--loop`: blijft draaien en voert run elke N uur uit
</span><span style="font-style:italic;color:#969896;">    &quot;&quot;&quot;
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#183691;">&quot;--loop&quot; </span><span style="font-weight:bold;color:#a71d5d;">in </span><span style="color:#323232;">sys</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">argv:
</span><span style="color:#323232;">        logger</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">info(</span><span style="color:#183691;">&quot;Loop‑modus geactiveerd (interval </span><span style="color:#0086b3;">%d</span><span style="color:#183691;"> uur)&quot;</span><span style="color:#323232;">, </span><span style="color:#0086b3;">RUN_INTERVAL_HOURS</span><span style="color:#323232;">)
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">import </span><span style="color:#323232;">schedule
</span><span style="color:#323232;">        schedule</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">every(</span><span style="color:#0086b3;">RUN_INTERVAL_HOURS</span><span style="color:#323232;">)</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">hours</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">do(run_once)
</span><span style="color:#323232;">        </span><span style="font-weight:bold;color:#a71d5d;">while </span><span style="color:#0086b3;">True</span><span style="color:#323232;">:
</span><span style="color:#323232;">            schedule</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">run_pending()
</span><span style="color:#323232;">            time</span><span style="font-weight:bold;color:#a71d5d;">.</span><span style="color:#323232;">sleep(</span><span style="color:#0086b3;">60</span><span style="color:#323232;">)
</span><span style="color:#323232;">    </span><span style="font-weight:bold;color:#a71d5d;">else</span><span style="color:#323232;">:
</span><span style="color:#323232;">        run_once()
</span><span style="color:#323232;">
</span><span style="color:#323232;">
</span><span style="font-weight:bold;color:#a71d5d;">if </span><span style="color:#323232;">__name__ </span><span style="font-weight:bold;color:#a71d5d;">== </span><span style="color:#183691;">&quot;__main__&quot;</span><span style="color:#323232;">:
</span><span style="color:#323232;">    main()
</span></pre>

      </div>
    </main>
  </body>
</html>
