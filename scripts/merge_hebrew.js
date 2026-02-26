const fs = require('fs');
const path = require('path');

function main() {
    const scriptDir = __dirname;
    const hebrewPackPath = path.join(scriptDir, '..', 'hebrew_pack.js');
    const hebrewPackNewPath = path.join(scriptDir, 'hebrew_pack_new.json');

    console.log("Reading existing hebrew_pack.js...");
    const oldContent = fs.readFileSync(hebrewPackPath, 'utf8');

    // Extract the object part
    const jsonStr = oldContent.replace(/^[\s\S]*?const HEBREW_PACK = /, '').replace(/;?\s*$/, '');

    // Use eval or new Function because it's a JS object, not strict JSON
    const oldPack = (new Function('return ' + jsonStr))();

    console.log("Reading new translations from hebrew_pack_new.json...");
    const newPack = JSON.parse(fs.readFileSync(hebrewPackNewPath, 'utf8'));

    // Merge: newPack goes first, then oldPack overwrites it to keep manual translations intact
    const mergedPack = { ...newPack, ...oldPack };

    const count = Object.keys(mergedPack).length;
    console.log(`Merged! Total problems in Hebrew pack: ${count}`);

    const newFileContent = `// Hebrew Language Pack for CodingZone Exercises\nconst HEBREW_PACK = ${JSON.stringify(mergedPack, null, 4)};\n`;

    fs.writeFileSync(hebrewPackPath, newFileContent, 'utf8');
    console.log("Saved complete translations to hebrew_pack.js!");
}

main();
