export function calcDuration(durationInMs: number): string {
  const duration_sec = Math.round(durationInMs / 1000);

  const min = Math.floor(duration_sec / 60);
  const sec = duration_sec % 60;

  return `${min}:${sec.toLocaleString("en-US", { minimumIntegerDigits: 2 })}`;
}
