const fs = require('fs');

function main() {
    console.log("Reading existing hebrew_pack.js...");
    const oldContent = fs.readFileSync('hebrew_pack.js', 'utf8');

    // Extract the object part
    const jsonStr = oldContent.replace(/^[\s\S]*?const HEBREW_PACK = /, '').replace(/;?\s*$/, '');

    // Use eval or new Function because it's a JS object, not strict JSON
    const oldPack = (new Function('return ' + jsonStr))();

    console.log("Reading new translations from hebrew_pack_new.json...");
    const newPack = JSON.parse(fs.readFileSync('hebrew_pack_new.json', 'utf8'));

    // Merge: newPack goes first, then oldPack overwrites it to keep manual translations intact
    const mergedPack = { ...newPack, ...oldPack };

    const count = Object.keys(mergedPack).length;
    console.log(`Merged! Total problems in Hebrew pack: ${count}`);

    const newFileContent = `// Hebrew Language Pack for CodingZone Exercises
const HEBREW_PACK = ${JSON.stringify(mergedPack, null, 4)};
`;

    fs.writeFileSync('hebrew_pack.js', newFileContent, 'utf8');
    console.log("Saved complete translations to hebrew_pack.js!");
}

main();
