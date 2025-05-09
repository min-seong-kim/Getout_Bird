import React, { useEffect, useState } from 'react';

const latest_audio = () => {
  const [audios, setAudios] = useState([]);

  useEffect(() => {
    fetch('http://220.149.235.221:4000/api/sounds')
      .then(res => res.json())
      .then(fileList => {
        const sorted = fileList
          .filter(name => name.endsWith('.wav') || name.endsWith('.mp3'))
          .sort((a, b) => {
            const getTime = f => {
              const match = f.match(/(\d+)/);
              return match ? parseInt(match[1]) : 0;
            };
            return getTime(b) - getTime(a);
          });

        const fullData = sorted.map(name => ({
          name,
          url: `http://220.149.235.221:4000/sounds/${name}`,
          timestamp: parseInt(name.match(/(\d+)/)?.[1] || 0),
        }));

        setAudios(fullData);
      })
      .catch(err => {
        console.error("❌ 오디오 불러오기 실패:", err);
      });
  }, []);

  const formatDate = (ts) => {
    const date = new Date(ts);
    return isNaN(ts) ? "날짜 정보 없음" : date.toLocaleString('ko-KR');
  };

  return (
    <div className="p-6 max-w-screen-xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">전체 저장된 오디오 목록</h1>
      <div className="grid grid-cols-2 gap-6">
        {audios.length === 0 ? (
          <div className="text-gray-500">불러올 오디오가 없습니다.</div>
        ) : (
          audios.map((audio, idx) => (
            <div key={idx} className="border p-4 space-y-2 text-center">
              <div className="text-sm font-semibold">{audio.name}</div>
              <div className="text-xs text-gray-500">{formatDate(audio.timestamp)}</div>
              <audio controls className="w-full">
                <source src={audio.url} />
                브라우저가 오디오 태그를 지원하지 않습니다.
              </audio>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default latest_audio;