export async function fetchImageList() {
  const res = await fetch('http://220.149.235.221:4000/api/images');
  const fileList = await res.json();

  const sorted = fileList
    .filter(name => name.startsWith('frame_') && name.endsWith('.jpg'))
    .sort((a, b) => {
      const getTime = f => {
        const match = f.match(/frame_(\d+)\.jpg/);
        return match ? parseInt(match[1]) : 0;
      };
      return getTime(b) - getTime(a);
    });

  return sorted.map(name => ({
    name,
    url: `http://220.149.235.221:4000/images/${name}`,
    timestamp: parseInt(name.match(/frame_(\d+)\.jpg/)[1])
  }));
}


export async function fetchImageList_result() {
  const res = await fetch('http://220.149.235.221:4000/api/images_result');
  const fileList = await res.json();

  const sorted = fileList
    .filter(name => name.startsWith('frame_') && name.endsWith('.jpg'))
    .sort((a, b) => {
      const getTime = f => {
        const match = f.match(/frame_(\d+)\.jpg/);
        return match ? parseInt(match[1]) : 0;
      };
      return getTime(b) - getTime(a);
    });

  return sorted.map(name => ({
    name,
    url: `http://220.149.235.221:4000/images_result/${name}`,
    timestamp: parseInt(name.match(/frame_(\d+)\.jpg/)[1])
  }));
}
