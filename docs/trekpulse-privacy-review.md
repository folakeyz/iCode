# TrekPulse privacy publication review

Reviewed October 2, 2026. This is an implementation review, not certification of legal compliance or Google Play approval.

## Confirmed identity and practices

- App: TrekPulse. Google Play developer: folaranmi.
- Contact: gbengaobafemi1@gmail.com.
- Public policy: https://icode-site.netlify.app/privacy.
- Owner confirmed minimum age 13, immediate deletion, and online step synchronization for leaderboards.
- Current source sends `dateKey`, `steps`, `calories`, and `distanceKm` to the server. The last two are derived from step counts. They remain disclosed; describing all health data as device-only would be inaccurate.
- Additional Health screen readings are read/displayed locally. Android requests steps, heart rate, weight, sleep and oxygen; iOS requests the equivalent HealthKit types. Android currently reads heart rate, sleep and weight; iOS reads heart rate, weight and oxygen.
- `server/services/accountDeletion.js` removes the account, steps, tokens, sessions, OTPs, user-linked audit records, authored messages and memberships. Groups with remaining members may transfer ownership.

## Items that policy text cannot resolve

1. **Submitted build and health permissions:** The current Android manifest declares steps and background health access, while the Health screen requests additional types. Align the release manifest, runtime requests and Play Console declarations with the features actually shipped. Do not add unused permissions merely to match the policy.
2. **Consent and leaderboard visibility:** Verify a prominent disclosure and affirmative consent before health access/background collection and before health-derived totals become visible to other users. A policy link alone is insufficient. Source shows a global leaderboard; do not claim sharing occurs only after separately joining a group.
3. **In-app policy and deletion:** Verify the exact public policy URL and a working account-deletion entry point are accessible in the submitted app. A settings title mentioning privacy is not proof of a policy link.
4. **Deletion scope:** Immediate deletion is described for the active application database, consistent with source. Verify production deletion, backup settings, infrastructure/application logs, uploaded files and any third-party copies. Do not promise immediate deletion of every copy without operational evidence. Source contains step-count logging, so infrastructure log retention deserves particular attention.
5. **Age and ads:** Verify the minimum age is enforced, the store target-audience settings agree, any required parental consent is implemented, and advertising treatment is appropriate for minors and the countries served.
6. **SDKs and vendors:** Verify the release SDK inventory and actual hosting/database/email/notification providers. Confirm the policy's no-health-data-sale and no-health-ad-targeting commitments operationally. AdMob can collect identifiers, coarse location inferred from IP, interactions and diagnostics independently of app code.
7. **Data safety and health declarations:** Complete the Health apps declaration and reconcile all Data safety answers, including off-device steps/derived metrics, account details, user content, identifiers and SDK collection. Device-only access still belongs in the privacy policy even when not classified as collection for Data safety.
8. **Deployment:** Deploy this static site to Netlify, then check `/privacy` in an unauthenticated browser. Confirm no login, geographic restrictions, PDF redirect or inaccessible route. Recheck the account deletion URL on the live backend.
9. **Jurisdictions:** Verify any additional jurisdiction-specific disclosures, legal bases, transfer safeguards, controller details and rights procedures for the countries where TrekPulse is offered. The source and owner confirmations do not establish every legal requirement.

## Suggested in-app disclosure to adapt and verify

“TrekPulse reads your steps from Health Connect or your phone’s activity sensors to track activity and calculate progress. With background access enabled, it can read steps when you are not using the app. Daily steps and calculated distance/calorie estimates sync to your TrekPulse account. Your profile and step totals can appear on leaderboards visible to other users. You can manage permissions in your device settings and delete your account and associated data.”

Display before the relevant access; provide affirmative consent and a decline option. Request additional Health screen metrics separately with an explanation of local use. This document does not implement those app changes.

## Official references

- [Google Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)
- [Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en)
- [Android health permissions guidance](https://support.google.com/googleplay/android-developer/answer/12991134?hl=en-GB)

## Validation boundary

Website checks cover HTML structure, local destinations, responsive layouts and mobile navigation. They do not establish production app behavior, deletion across infrastructure, Play Console declarations or Google approval.
