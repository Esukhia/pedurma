# Changelog

<!--next-version-placeholder-->

## v0.1.27 (2021-07-15)
### Fix
* **reconstruction:** Tibetan serial number added to notes ([`f992aee`](https://github.com/Esukhia/pedurma/commit/f992aee12d10419716f700ebc9334babe0aa5043))

## v0.1.26 (2021-07-13)
### Fix
* **reconstruction:** Page number in img changed to |pg_num| to not confuse with p tag ([`b3ba0b0`](https://github.com/Esukhia/pedurma/commit/b3ba0b01f8b2459f07a0e7eced9da99d65c89040))

## v0.1.25 (2021-07-12)
### Fix
* **docx:** Custom path enabled ([`51947e3`](https://github.com/Esukhia/pedurma/commit/51947e3d279bfb002893e1d7ebec06576a7eb77f))

## v0.1.24 (2021-07-09)
### Fix
* **reconstruction:** Docx preview enable ([`0c5ce98`](https://github.com/Esukhia/pedurma/commit/0c5ce98210c5f7d75ec8d0ceb7fb58ec2e07a305))

## v0.1.23 (2021-07-08)
### Fix
* **reconstruction:** The note marker in namsel durchen are changed to <u ([`0f762c8`](https://github.com/Esukhia/pedurma/commit/0f762c8506a606cedee2d95b6b5724516c9f1dd3))

## v0.1.22 (2021-07-05)
### Fix
* **reconstruction:** Preprocessing footnote excluded ([`687eca5`](https://github.com/Esukhia/pedurma/commit/687eca50380ceb70dbf5f92af89a0ddb38d6af7f))

## v0.1.21 (2021-07-04)
### Fix
* **reconstruction:** Page num undetected expection handled ([`2d42fe8`](https://github.com/Esukhia/pedurma/commit/2d42fe8fe4daa3d4cc3bca02cc518e43250cd7a6))

## v0.1.20 (2021-07-01)
### Fix
* **nalanda:** Collation text generation code added ([`9c595a7`](https://github.com/Esukhia/pedurma/commit/9c595a7eee4192ec4a0e6f6038086eea22b4384f))

## v0.1.19 (2021-07-01)
### Fix
* **test:** Test for nalanda text reinsertion added ([`343bee1`](https://github.com/Esukhia/pedurma/commit/343bee1148488c793cbcde07e73fe327ab94e62d))
* **test:** Nalanda text test pass ([`b2a8cd3`](https://github.com/Esukhia/pedurma/commit/b2a8cd39a14cbe0db85730b79544f93e4b343da6))
* **nalanda:** Nalanda text reinsertion code added ([`63d84cc`](https://github.com/Esukhia/pedurma/commit/63d84cc127012d865bdb57a914465e32bf6e7ef7))
* **pagewithnote:** Nalanda use case adaptations added ([`d2128bf`](https://github.com/Esukhia/pedurma/commit/d2128bf1bec41bfa2eefa851f858972b0de04ebf))

## v0.1.18 (2021-06-28)
### Fix
* **reconstruction:** Drege-google and namsel pecha ids updated ([`c99abf7`](https://github.com/Esukhia/pedurma/commit/c99abf7c734c4dda60d4023a21d622bb8eae612b))
* **preview:** Preview is given in derge line break of the text ([`3570146`](https://github.com/Esukhia/pedurma/commit/35701466efc5c2743162a22a6e6ef9b6d43a1c09))

## v0.1.17 (2021-05-26)
### Fix
* **setup:** Pylibyaml included in setup ([`7e6b032`](https://github.com/Esukhia/pedurma/commit/7e6b032cf485c40c386cc3b8820a4b918b1734c3))
* **yaml:** Replaced safe_load and safe_dump using CLoader and CDumper ([`24af85a`](https://github.com/Esukhia/pedurma/commit/24af85a591f94af913141c322e14b91d9741ba53))
* **save-text:** Not including body while save for google text excluded ([`f5ee1a5`](https://github.com/Esukhia/pedurma/commit/f5ee1a557f07162b4e066cc85c809516d044afeb))

## v0.1.16 (2021-05-17)
### Fix
* **readme:** Readme update ([`19256ab`](https://github.com/Esukhia/pedurma/commit/19256abc9a65a5605f4cef71ef093579fd642602))

## v0.1.15 (2021-05-17)
### Fix
* **reconstruction:** Preview of whole text can be extracted ([`93cc5fd`](https://github.com/Esukhia/pedurma/commit/93cc5fd3690ad53cf28cfe6ad5ad4a2274a78c44))

## v0.1.14 (2021-05-14)
### Fix
* **pagination update:** Invalid page ref are ignored during pagination update ([`88beeb4`](https://github.com/Esukhia/pedurma/commit/88beeb43afc92276d60e475902be4f22ae90bea9))

## v0.1.13 (2021-05-13)
### Fix
* **get_preview:** Page missing exception raised ([`90626c8`](https://github.com/Esukhia/pedurma/commit/90626c8e076f48b89ad61bc61698dd6b91f82d9d))

## v0.1.12 (2021-05-12)
### Fix
* **reconstruction:** Page number missing exception added ([`4fbdf10`](https://github.com/Esukhia/pedurma/commit/4fbdf1029f050c1395a21c18abd5d9b31f0bc67d))

## v0.1.11 (2021-05-10)
### Fix
* **save-text:** Accept optional kwargs of download_pecha ([`782d076`](https://github.com/Esukhia/pedurma/commit/782d076b523f63fe541472318d5893c0d9613538))

## v0.1.10 (2021-05-10)
### Fix
* **texts:** Removed vol_span attribute as it can be obtain by using text uuid and pecha idx ([`8e3f578`](https://github.com/Esukhia/pedurma/commit/8e3f5785bbb7d5e1735af052a447c35d5a6cfa96))

## v0.1.9 (2021-05-10)
### Fix
* **save_text:** Pecha-opf path obtained from download pecha method ([`f5bca1a`](https://github.com/Esukhia/pedurma/commit/f5bca1a8a111336dbf67d4769e68abd0894c132e))

## v0.1.8 (2021-05-09)
### Fix
* **save_text:** Added update opf method ([`0dd4e9d`](https://github.com/Esukhia/pedurma/commit/0dd4e9d2948f87b7fe16efc53eef84de04b44d9f))

## v0.1.7 (2021-05-09)
### Fix
* **index-update:** Index update method implemented ([`002e247`](https://github.com/Esukhia/pedurma/commit/002e247213b41f5830cb7e839ff23f0836aa96a2))
* **text:** Serializing only durchen and pagination annotation ([`6643938`](https://github.com/Esukhia/pedurma/commit/6643938d37e23602d875b9dfb76c133c775813e2))
* **save_text:** Saving text feature added ([`a1c9535`](https://github.com/Esukhia/pedurma/commit/a1c9535280af54acbb38bfbab35224cc867ef5ee))

## v0.1.6 (2021-05-06)
### Fix
* **notes:** Removed redundant methods ([`c48c66d`](https://github.com/Esukhia/pedurma/commit/c48c66d19b163a7c05b574d21a74139b86eef077))

## v0.1.5 (2021-05-06)
### Fix
* **text-obj:** Durchen not found bug fix ([`30afa6a`](https://github.com/Esukhia/pedurma/commit/30afa6ae2ab2e8dfb6c441e9fdf3464a7a6cfb48))

## v0.1.4 (2021-05-05)
### Fix
* **reconstruction:** Pg ref bug fixed ([`9023d3e`](https://github.com/Esukhia/pedurma/commit/9023d3e8b698c502cf3bac7f801ae882a7f7d70d))

## v0.1.3 (2021-05-05)
### Fix
* **test-case:** Test case added for text obj generator ([`d044ead`](https://github.com/Esukhia/pedurma/commit/d044ead102ab54fc0902e570fc527fa52b0baf3f))

## v0.1.2 (2021-05-05)
### Fix
* **text:** Text module added ([`fd77eae`](https://github.com/Esukhia/pedurma/commit/fd77eae6d76be9d649fd9306edc12f97fcc4c2ec))

## v0.1.1 (2021-05-05)
### Fix
* **hot-fix:** Double mid syl marker index out of range bug ([`fe32659`](https://github.com/Esukhia/pedurma/commit/fe32659b39804ea79c1f2e558ade277dcd28a5a4))
* **readme:** Publish ([`deef949`](https://github.com/Esukhia/pedurma/commit/deef94989efc4f0aca4e24bbb8c093a5026fb59a))
* **setup:** Python version changed ([`46cbd3c`](https://github.com/Esukhia/pedurma/commit/46cbd3c152d26b5bd968944cf932dac8779b192b))
* **readme:** Readme updated ([`b5bdf81`](https://github.com/Esukhia/pedurma/commit/b5bdf81630918d6478b15f4e7f0b232a30596409))
* **pedurma:** Code added ([`1e8a969`](https://github.com/Esukhia/pedurma/commit/1e8a9692194f4c95e005bf40340075686a56fba1))
