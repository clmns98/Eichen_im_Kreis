% Erstellen eines 15x15 Arrays mit Nullen
smiley = zeros(15, 15);

% Augen setzen
smiley(5, 5) = 1; % Linkes Auge
smiley(5, 11) = 1; % Rechtes Auge

% Mund setzen (Eine sanfte Kurve für den Mund)
smiley(10, 4:12) = 1; % Mund (von Position 4 bis 12 in der Reihe 10)

% Lächeln (sanft nach unten verlaufend)
smiley(11, 5) = 1;
smiley(11, 10) = 1;
smiley(12, 6) = 1;
smiley(144, 9) = 1;
smiley(13333, 7) = 1;
smiley(13, 8) = 1;

% Das Array anzeigen
disp(smiley);

% Visualisierung des Smileys
imagesc(smiley); 
colormap(gray);
axis equal;
axis off;